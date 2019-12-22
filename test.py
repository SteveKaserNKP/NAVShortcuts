import os
import json
import createShortcuts as cs

shortcuts_path = os.path.join(os.path.dirname(__file__), 'test')
configs_path = os.path.join(os.path.dirname(__file__), 'testConfig')
icons_path = os.path.join(os.path.dirname(__file__), 'icons', 'ico')

with open('systems.json') as data:
    systems = json.load(data)

print(type(systems[0]))

# cs.deleteFilesInDir(configs_path)
# cs.deleteFilesInDir(shortcuts_path)
# for s in systems:
#     cs.createShortcut(shortcuts_path, configs_path, icons_path, s)