import tkinter as tk
import os
import json
from iconFrame import IconFrame

icon_size = 75
icon_2009R2 = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_2009R2_{icon_size}.png')
icon_windows = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_windows_{icon_size}.png')
icon_web = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_web_{icon_size}.png')
icons = []

with open('systems.json') as data:
    systems = json.load(data)

def getIconFile(version, client):
    if version == '2009R2':
        return icon_2009R2
    else:
        return icon_web if client == 'WEB' else icon_windows

def getName(data):
    if data['Client'] == 'WEB':
        rName = f"{data['SystemName']} - WEB - {data['NavisionVersion']} - SQL@{data['SQLServer']}"
    else:
        rName = f"{data['SystemName']} - {data['NavisionVersion']} - SQL@{data['SQLServer']}"
    if data['NavisionVersion'] == '2009R2':
        rName = rName + f" - {data['Company']}"
    else:
        rName = rName + f" - RTC@{data['RTCServer']} - {data['ClientServicesPort']}"
        if data['Profile']:
            rName = rName + f" - {data['Profile']}"
        if data['Configure'] == 'Y':
            rName = rName + f" - CONFIGURE"
        rName = rName
    return rName

def iconDoubleClick(event):
    # get the name of the parent
    parent = event.widget.winfo_parent()
    print(parent)
    # use the name of the parent to get the actual parent's object,
    # then use that to pull the data from it
    data = event.widget._nametowidget(parent).data
    print(f'from label: {data}')

def doubleClick(event):
    print(event.widget.data)

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('800x600')

c = 0
r = 0
stack = 10
for i in range(len(systems)):
    data = systems[i]
    c = i % stack
    if i > 0 and i % stack == 0:
        r+=1
    # FRAME
    frame = tk.Frame(window, relief=tk.RIDGE, padx=0, pady=5, bd=1)
    frame.bind('<Double-Button-1>', doubleClick)
    frame.keys().append('data')
    frame.data = data

    # ICON
    img = tk.PhotoImage(file=getIconFile(data['NavisionVersion'], data['Client']))
    icons.append(img)
    icon_lbl = tk.Label(frame, image=icons[i])
    icon_lbl.bind('<Double-Button-1>', iconDoubleClick)

    # TEXT
    text_lbl = tk.Label(frame, text=getName(data), wraplength=100)
    text_lbl.bind('<Double-Button-1>', iconDoubleClick)

    # pack objects
    frame.grid(column=c, row=r, padx=2, pady=2)
    icon_lbl.grid(column=0, row=0)
    text_lbl.grid(column=0, row=1)

window.mainloop()