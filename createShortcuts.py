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

def deleteShortcuts(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def createShortcuts(path, systems):
    for s in systems:
        lnk_path = os.path.join(path, lnkName(s))
        # this only creates 2018 shortcuts - needs to determine version
        lnk_target = os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV","110","RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
        winshell.CreateShortcut(Path=lnk_path,
                                Target=lnk_target,
                                Arguments='',
                                StartIn='',
                                Icon=('',0),
                                Description=''
                                )

with open('systems.json') as data:
    systems = json.load(data)

deleteShortcuts(path)
createShortcuts(path, systems)