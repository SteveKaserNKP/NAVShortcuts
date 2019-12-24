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

def createIconFrame(master, data, icons, icon_paths, c, r):
    # create objects
    frame = createFrame(master, data)
    icon_lbl, icons = createIconLabel(frame, data, icons, icon_paths)
    text_lbl = createTextLabel(frame, data)
    # pack objects
    frame.grid(column=c, row=r, padx=2, pady=2)
    icon_lbl.grid(column=0, row=0)
    text_lbl.grid(column=0, row=1)

def createFormEntry(master, name, c, r, lbl_font, entry_font, state=tk.NORMAL):
    frame = tk.Frame(master)
    frame.grid(column=c, row=r, pady=5, sticky='EW')
    lbl = tk.Label(frame, text=name, font=lbl_font, state=state)
    var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=var, font=entry_font, state=state)
    lbl.grid(column=0, row=0, sticky='W')
    entry.grid(column=0, row=1)

def createOptionMenu(master, name, options, c, r, lbl_font, options_font, state=tk.NORMAL):
    frame = tk.Frame(master)
    frame.grid(column=c, row=r, pady=5, sticky='EW')
    lbl_options = tk.Label(frame, text=name, font=lbl_font, state=state)
    var_options = tk.StringVar(frame)
    var_options.set(options[0])
    options = tk.OptionMenu(frame, var_options, *options)
    options.configure(state=state)
    options_menu = options.nametowidget(options.menuname)
    options_menu.configure(font=options_font)
    lbl_options.grid(column=0, row=0, sticky='W')
    options.grid(column=0, row=1, sticky='W')

def createCheckbox(master, name, c, r, check_font, state=tk.NORMAL):
    frame = tk.Frame(master)
    frame.grid(column=c, row=r, pady=5, sticky='EW')
    var_checkbox = tk.IntVar()
    checkbox = tk.Checkbutton(frame, text=name, font=check_font, variable=var_checkbox, state=state)
    checkbox.grid(column=0, row=1)

def createFormFrame(master, name, c, r):
    f = tk.LabelFrame(master, text=name)
    f.grid(column=c, row=r, pady=5, ipadx=5, ipady=5, sticky='EW')
    return f