import os
import winshell
import paths

def getSQLName(s):
    if "\\" in s:
        return s[:s.index("\\")]
    else:
        return s

def getLnkPath(s):
    if s['Client'] == 'WEB':
        rName = f"{s['SystemName']} - WEB - {s['NavisionVersion']} - SQL@{getSQLName(s['SQLServer'])}"
    else:
        rName = f"{s['SystemName']} - {s['NavisionVersion']} - SQL@{getSQLName(s['SQLServer'])}"
    if s['NavisionVersion'] == '2009R2':
        return rName
    else:
        rName = rName + f" - RTC@{s['RTCServer']} - {s['ClientServicesPort']}"
        if s['Profile']:
            rName = rName + f" - {s['Profile']}"
        if s['Configure'] == 'Y':
            rName = rName + f" - CONFIGURE"
        return rName

def getTargetVersion(s):
    version = s['NavisionVersion']
    client = s['Client']
    if version == "2009R2":
        return paths.exe_2009R2
    else:
        if client == 'WEB':
            return paths.exe_ie
        else:
            if version == "2016":
                return paths.exe_2016
            elif version == "2017":
                return paths.exe_2017
            elif version == "2018":
                return paths.exe_2018
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
    args = []
    if version == "2009R2":
        args.append(f"servername={sql}")
        args.append(f"database={db}")
        if company:
            args.append(f"company={company}")
        if reqAuth:
            args.append(f"ntauthentication={'yes' if reqAuth == 'Y' else 'no'}")
        return args
    else:
        if client == 'WEB':
            if port:
                args.append(f"http://{rtc}.nkparts.com:{port}/{instance}")
                return args
            else:
                args.append(f"http://{rtc}.nkparts.com/{instance}")
                return args
        else:
            config = createCUS(rtc, port, instance, path)
            args.append(f'-settings:"{os.path.join(path, config)}"')
            if s['Profile']:
                args.append(f'-profile:"{profile}"')
            if s['Configure']:
                args.append("-configure")
            return args

def argsJoin(s, configs):
    args = getArgs(s, configs)
    if s['NavisionVersion'] == '2009R2':
        return (', ').join(args)
    else:
        if s['Client'] == 'WEB':
            return args[0]
        else:
            return (' -').join(args)

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
    shortcut_name = getLnkPath(system) + '.lnk'
    lnk_path = os.path.join(path_shortcuts, shortcut_name)
    lnk_target = getTargetVersion(system)
    lnk_args = argsJoin(system, path_configs)
    lnk_icon = getIcon(system, path_icons)
    winshell.CreateShortcut(
        Path=lnk_path,
        Target=lnk_target,
        Arguments=lnk_args,
        StartIn='',
        Icon=(lnk_icon,0),
        Description=''
    )