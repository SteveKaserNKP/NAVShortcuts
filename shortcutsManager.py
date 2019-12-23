import tkinter as tk
import os
import json
from iconFrame import IconFrame

icon_size = 75
icon_2009R2 = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_2009R2_{icon_size}.png')
icon_windows = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_windows_{icon_size}.png')
icon_web = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_web_{icon_size}.png')

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
        rName = rName
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
    data = event.widget._nametowidget(parent).getvar('data')
    print(f'from label: {data}')

def doubleClick(event):
    d = event.widget.getvar('data')
    print(f'from frame: {d}')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('800x600')

i = 0
data = systems[i]
# FRAME
frame = tk.Frame(window, relief=tk.RIDGE, padx=0, pady=5, bd=1)
frame.bind('<Double-Button-1>', doubleClick)
frame.setvar('data', data)
# ICON
img = tk.PhotoImage(file=getIconFile(data['NavisionVersion'], data['Client']))
icon_lbl = tk.Label(frame, image=img)
icon_lbl.bind('<Double-Button-1>', lambda e: iconDoubleClick(e))

# TEXT
text_lbl = tk.Label(frame, text=getName(data), wraplength=100)
text_lbl.bind('<Double-Button-1>', lambda e: iconDoubleClick(e))

# pack objects
frame.grid(column=i, row=0, padx=2, pady=2)
icon_lbl.grid(column=0, row=0)
text_lbl.grid(column=0, row=1)

i+=1
data1 = systems[i]
# FRAME
frame1 = tk.Frame(window, relief=tk.RIDGE, padx=0, pady=5, bd=1)
frame1.bind('<Double-Button-1>', doubleClick)
frame1.setvar('data', data1)

# ICON
img1 = tk.PhotoImage(file=getIconFile(data['NavisionVersion'], data['Client']))
icon_lbl1 = tk.Label(frame1, image=img1)
icon_lbl1.bind('<Double-Button-1>', lambda e: iconDoubleClick(e))

# TEXT
text_lbl1 = tk.Label(frame1, text=getName(data), wraplength=100)
text_lbl1.bind('<Double-Button-1>', lambda e: iconDoubleClick(e))

# pack objects
frame1.grid(column=i, row=0, padx=2, pady=2)
icon_lbl1.grid(column=0, row=0)
text_lbl1.grid(column=0, row=1)



# frame = createFrame(window, systems[10])
# frame.grid(column=0, row=0, padx=2, pady=2)
# icon_lbl = createIconLabel(frame, icon_windows)
# icon_lbl.grid(column=0, row=0, padx=10, pady=5)
# text_lbl = createTextLabel(frame, getName(systems[10]))
# text_lbl.grid(column=0, row=1)
# img = tk.PhotoImage(file=getIconFile(systems[10]['NavisionVersion'], systems[10]['Client']))
# icon_lbl = tk.Label(frame, image=img)
# icon_lbl.bind('<Double-Button-1>', iconDoubleClick)
# icon_lbl.grid(column=0, row=0)

window.mainloop()