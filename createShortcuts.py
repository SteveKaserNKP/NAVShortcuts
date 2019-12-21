import os
import sys
import glob
import winshell
import json

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
            rName = rName + f" - {s['Configure']}"
        return rName + '.lnk'

path = os.path.join(os.path.dirname(__file__), "test")

with open('systems.json') as data:
    systems = json.load(data)

for s in systems:
    lnk_path = os.path.join(path, lnkName(s))
    lnk_target = ''
    # winshell.CreateShortcut(Path=)

