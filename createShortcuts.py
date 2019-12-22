import os
import winshell
from urllib.parse import urljoin
import webbrowser
import json

shortcuts_path = os.path.join(os.path.dirname(__file__), "test")
configs_path = os.path.join(os.path.dirname(__file__), "testConfig")
icons_path = os.path.join(os.path.dirname(__file__), "icons")

def getSQLName(s):
    if "\\" in s:
        return s[:s.index("\\")]
    else:
        return s

def getLnkPath(s, path):
    if s['Client'] == 'WEB':
        rName = f"{s['SystemName']} - WEB - {s['NavisionVersion']} - SQL@{getSQLName(s['SQLServer'])}"
    else:
        rName = f"{s['SystemName']} - {s['NavisionVersion']} - SQL@{getSQLName(s['SQLServer'])}"
    if s['NavisionVersion'] == '2009R2':
        rName = rName + '.lnk'
    else:
        rName = rName + f" - RTC@{s['RTCServer']} - {s['ClientServicesPort']}"
        if s['Profile']:
            rName = rName + f" - {s['Profile']}"
        if s['Configure'] == 'Y':
            rName = rName + f" - CONFIGURE"
        rName = rName + '.lnk'
    return os.path.join(path, rName)

def getTargetVersion(s):
    version = s['NavisionVersion']
    client = s['Client']
    if version == "2009R2":
        return os.path.join("C:","Program Files (x86)","Microsoft Dynamics NAV","60","Classic","finsql.exe")
    else:
        if client == 'WEB':
            return 'c:\\program files\\internet explorer\\iexplore.exe'
        else:
            if version == "2016":
                return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","90","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
            elif version == "2017":
                return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","100","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
            elif version == "2018":
                return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","110","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
            else:
                return f'unsupported version passed in to getTargetVersion: {version}'

def getArgs(s, path):
    sql = s['SQLServer']
    db = s['DatabaseName']
    version = s['NavisionVersion']
    company = s['Company']
    reqAuth = s['RequireAuthentication']
    client = s['Client']
    rtc = s['RTCServer']
    port = s['ClientServicesPort']
    instance = s['ServerInstanceName']
    profile = s['Profile']
    if version == "2009R2":
        args = f"servername={sql}, database={db}"
        if company:
            args = args + f", company={company}"
        if reqAuth:
            args = args + f", ntauthentication={'yes' if reqAuth == 'Y' else 'no'}"
        return args
    else:
        if client == 'WEB':
            if port:
                return f"http://{rtc}.nkparts.com:{port}/{instance}"
            else:
                return f"http://{rtc}.nkparts.com:{port}/{instance}"
        else:
            config = createCUS(rtc, port, instance, path)
            args = f' -settings:"{os.path.join(configs_path, config)}"'
            if s['Profile']:
                args = args + f' -profile:"{profile}"'
            if s['Configure']:
                args = args + " -configure"
            return args

def createCUS(rtc, port, instance, path):
    config_name = f"{instance}_{rtc}_{port}.config"

    config_text = (
        f'<?xml version="1.0" encoding="utf-8"?>\n'
        f'<configuration>\n'
        f'    <appSettings>\n'
        f'        <add key="Server" value="{rtc}.nkparts.com" />\n'
        f'        <add key="ClientServicesPort" value="{port}" />\n'
        f'        <add key="ServerInstance" value="{instance}" />\n'
        f'        <add key="TenantId" value="" />\n'
        f'        <add key="ClientServicesProtectionLevel" value="EncryptAndSign" />\n'
        f'        <add key="UrlHistory" value="" />\n'
        f'        <add key="ClientServicesCompressionThreshold" value="64" />\n'
        f'        <add key="ClientServicesChunkSize" value="28" />\n'
        f'        <add key="MaxNoOfXMLRecordsToSend" value="500000" />\n'
        f'        <add key="MaxImageSize" value="26214400" />\n'
        f'        <add key="ClientServicesCredentialType" value="Windows" />\n'
        f'        <add key="ACSUri" value="" />\n'
        f'        <add key="AllowNtlm" value="true" />\n'
        f'        <add key="ServicePrincipalNameRequired" value="False" />\n'
        f'        <add key="ServicesCertificateValidationEnabled" value="true" />\n'
        f'        <add key="DnsIdentity" value="" />\n'
        f'        <add key="HelpServer" value="" />\n'
        f'        <add key="HelpServerPort" value="" />\n'
        f'        <add key="ProductName" value="" />\n'
        f'        <add key="UnknownSpnHint" value="" />\n'
        f'    </appSettings>\n'
        f'</configuration>'
    )
    
    with open(os.path.join(path, config_name), 'w') as config:
        config.write(config_text)

    return config_name

def getIcon(s, icons):
    version = s['NavisionVersion']
    client = s['Client']
    if version == '2009R2':
        return os.path.join(icons, 'icon_2009R2.ico')
    else:
        if client == 'WEB':
            return os.path.join(icons, 'icon_web.ico')
        else:
            return os.path.join(icons, 'icon_windows.ico')

def deleteFilesInDir(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def createShortcut(path_shortcuts, path_configs, path_icons, system):
    lnk_path = getLnkPath(system, path_shortcuts)
    lnk_target = getTargetVersion(system)
    lnk_args = getArgs(system, path_configs)
    lnk_icon = getIcon(system, path_icons)
    winshell.CreateShortcut(
        Path=lnk_path,
        Target=lnk_target,
        Arguments=lnk_args,
        StartIn='',
        Icon=(lnk_icon,0),
        Description=''
    )

with open('systems.json') as data:
    systems = json.load(data)

deleteFilesInDir(configs_path)
deleteFilesInDir(shortcuts_path)
for s in systems:
    createShortcut(shortcuts_path, configs_path, icons_path, s)