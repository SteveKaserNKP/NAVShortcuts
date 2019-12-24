import tkinter as tk
import paths
import shortcutUtils as sc_utils

systems = sc_utils.parseSystemsJSON('systems.json')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('1500x960')

form_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
form_frame.grid(column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='NESW')

calibri12 = ('Calibri', 12)
ebrima14 = ('Ebrima', 14)
nav_versions = ['                    ', '2009R2', '2016', '2017', '2018']
nav_clients = ['                    ', 'Windows', 'WEB']

def versionChange(*args):
    v = version.get()
    if v not in ['', '2009R2']:
        clients_label = clients.nametowidget(clients.winfo_parent()).children['!label']
        clients_label.configure(state=tk.NORMAL)
        clients.configure(state=tk.NORMAL)

# Shared options
frame_shared = sc_utils.createFormFrame(form_frame, 'Shared', 0, 0)
sys_name = sc_utils.createFormEntry(frame_shared, 'System Name', 0, 0, calibri12, ebrima14)
versions, version = sc_utils.createOptionMenu(frame_shared, 'Navision Version', nav_versions, 0, 1, calibri12, ebrima14)
version.trace('w', versionChange)
clients, client = sc_utils.createOptionMenu(frame_shared, 'Client', nav_clients, 0, 2, calibri12, ebrima14, tk.DISABLED)
sql_server = sc_utils.createFormEntry(frame_shared, 'SQL Server', 0, 3, calibri12, ebrima14)
# RTC Options
frame_rtc = sc_utils.createFormFrame(form_frame, 'RTC Options', 0, 1)
rtc_server = sc_utils.createFormEntry(frame_rtc, 'RTC Server', 0, 0, calibri12, ebrima14, tk.DISABLED)
port = sc_utils.createFormEntry(frame_rtc, 'Client Services Port', 0, 1, calibri12, ebrima14, tk.DISABLED)
instance = sc_utils.createFormEntry(frame_rtc, 'Server Instance Name', 0, 2, calibri12, ebrima14, tk.DISABLED)
use_profile = sc_utils.createCheckbox(frame_rtc, 'Use Profile', 0, 3, calibri12, tk.DISABLED)
profile_name = sc_utils.createFormEntry(frame_rtc, 'Profile Name', 0, 4, calibri12, ebrima14, tk.DISABLED)
configure = sc_utils.createCheckbox(frame_rtc, 'Create Configuration Shortcut', 0, 5, calibri12, tk.DISABLED)
# 2009R2 Options
frame_2009R2 = sc_utils.createFormFrame(form_frame, '2009R2 Options', 0, 2)
db_name = sc_utils.createFormEntry(frame_2009R2, 'Database Name', 0, 0, calibri12, ebrima14, tk.DISABLED)
company_name = sc_utils.createFormEntry(frame_2009R2, 'Company Name', 0, 1, calibri12, ebrima14, tk.DISABLED)
req_auth = sc_utils.createCheckbox(frame_2009R2, 'Require Authentication', 0, 2, calibri12, tk.DISABLED)

# Buttons
# def printData():
#     print(sys_name.get())
# frame_buttons = sc_utils.createFormFrame(form_frame, 'Buttons', 0, 3)
# btn = tk.Button(frame_buttons, text='Test', command=printData)
# btn.grid(column=0, row=0)


icon_size = 75
icon_paths = paths.iconPathsSize(icon_size, paths.icons_path_png)

icons_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
icons_frame.grid(column=1, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='NESW')

icons = []
c = 0
r = 0
stack = 10
for i in range(len(systems)):
    data = systems[i]
    c = i % stack
    if i > 0 and i % stack == 0:
        r+=1
    sc_utils.createIconFrame(icons_frame, data, icons, icon_paths, c, r)

window.mainloop()