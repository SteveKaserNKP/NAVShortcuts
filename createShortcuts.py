import os
import winshell
import json

path = os.path.join(os.path.dirname(__file__), "test")

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
        return ''

def deleteShortcuts(path):
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

deleteShortcuts(path)
createShortcuts(path, systems)