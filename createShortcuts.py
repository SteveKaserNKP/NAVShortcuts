import os
import winshell
import json

shortcuts_path = os.path.join(os.path.dirname(__file__), "test")
configs_path = os.path.join(os.path.dirname(__file__), "testConfig")

def getSQLName(s):
    if "\\" in s:
        return s[:s.index("\\")]
    else:
        return s

def lnkName(s):
    rName = f"{s['SystemName']} - {s['NavisionVersion']} - SQL@{getSQLName(s['SQLServer'])}"
    if s['NavisionVersion'] == '2009R2':
        return rName + '.lnk'
    else:
        rName = rName + f" - RTC@{s['RTCServer']} - {s['ClientServicesPort']}"
        if s['Profile']:
            rName = rName + f" - {s['Profile']}"
        if s['Configure'] == 'Y':
            rName = rName + f" - CONFIGURE"
        return rName + '.lnk'

def getTargetVersion(v):
    if v == "2009R2":
        return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","60","Classic","finsql.exe")
    elif v == "2016":
        return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","90","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
    elif v == "2017":
        return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","100","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
    elif v == "2018":
        return os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","110","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
    else:
        return f'unsupported version passed in to getTargetVersion: {v}'

def getArgs(s):
    v = s['NavisionVersion']
    if v == "2009R2":
        args = f"servername={s['SQLServer']}, database={s['DatabaseName']}"
        if s['Company']:
            args = args + f", company={s['Company']}"
        if s['RequireAuthentication']:
            args = args + f", ntauthentication={'yes' if s['RequireAuthentication'] == 'Y' else 'no'}"
        return args
    else:
        config = createCUS(s['RTCServer'], s['ClientServicesPort'], s['ServerInstanceName'], configs_path)
        args = f' -settings:"{os.path.join(configs_path, config)}"'
        if s['Profile']:
            profile = s['Profile']
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

def deleteFilesInDir(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def createShortcuts(path, systems):
    for s in systems:
        lnk_path = os.path.join(path, lnkName(s))
        lnk_target = getTargetVersion(s['NavisionVersion'])
        lnk_args = getArgs(s)
        winshell.CreateShortcut(Path=lnk_path,
                                Target=lnk_target,
                                Arguments=lnk_args,
                                StartIn='',
                                Icon=('',0),
                                Description=''
                                )

with open('systems.json') as data:
    systems = json.load(data)

deleteFilesInDir(configs_path)
deleteFilesInDir(shortcuts_path)
createShortcuts(shortcuts_path, systems)