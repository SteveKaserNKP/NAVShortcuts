import os
import sys
import glob
import winshell
import json

with open('systems.json') as data:
    systems = json.load(data)

print(systems)