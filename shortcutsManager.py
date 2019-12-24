import tkinter as tk
import os
import json
from iconFrame import IconFrame
import subprocess
import paths
import shortcutUtils as sc_utils

icon_size = 75
icon_paths = paths.iconPathsSize(icon_size, paths.icons_path_png)

with open('systems.json') as data:
    systems = json.load(data)

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('800x600')

icons = []
c = 0
r = 0
stack = 10
for i in range(len(systems)):
    data = systems[i]
    c = i % stack
    if i > 0 and i % stack == 0:
        r+=1
    # create objects
    frame = sc_utils.createFrame(window, data)
    icon_lbl, icons = sc_utils.createIconLabel(frame, data, icons, icon_paths)
    text_lbl = sc_utils.createTextLabel(frame, data)
    # pack objects
    frame.grid(column=c, row=r, padx=2, pady=2)
    icon_lbl.grid(column=0, row=0)
    text_lbl.grid(column=0, row=1)

window.mainloop()