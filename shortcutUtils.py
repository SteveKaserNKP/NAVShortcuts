import tkinter as tk
import os
import createShortcuts as cs
import paths
import subprocess
import json

def parseSystemsJSON(j):
    with open(j) as data:
        s = json.load(data)
    return s

def getIconFile(version, client, icon_paths):
    if version == '2009R2':
        return icon_paths['icon_2009R2']
    else:
        return icon_paths['icon_web'] if client == 'WEB' else icon_paths['icon_windows']

def iconDoubleClick(event):
    parent = event.widget.winfo_parent()
    data = event.widget._nametowidget(parent).data
    openNav(data)

def doubleClick(event):
    data = event.widget.data
    openNav(data)

def openNav(data):
    exe = cs.getTargetVersion(data)
    args = cs.argsJoin(data, paths.configs_path)
    runArgs = exe + ' ' + args
    subprocess.call(runArgs)

def createFrame(master, data):
    frame = tk.Frame(master, relief=tk.RIDGE, padx=0, pady=5, bd=1)
    frame.bind('<Double-Button-1>', doubleClick)
    frame.keys().append('data')
    frame.data = data
    return frame

def createIconLabel(master, data, icons, icon_paths):
    img = tk.PhotoImage(file=getIconFile(data['NavisionVersion'], data['Client'], icon_paths))
    icons.append(img)
    icon_lbl = tk.Label(master, image=icons[-1])
    icon_lbl.bind('<Double-Button-1>', iconDoubleClick)
    return (icon_lbl, icons)

def createTextLabel(master, data):
    text_lbl = tk.Label(master, text=cs.getLnkPath(data), wraplength=100)
    text_lbl.bind('<Double-Button-1>', iconDoubleClick)
    return text_lbl