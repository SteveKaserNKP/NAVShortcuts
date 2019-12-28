import tkinter as tk
import paths
import shortcutUtils as sc_utils

systems = sc_utils.parseSystemsJSON('systems.json')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('1680x960')

form_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
form_frame.grid(column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='NESW')

lbl_font = ('Calibri', 12)
entry_font = ('Ebrima', 14)

nav_versions = ['', '2009R2', '2016', '2017', '2018']
nav_clients = ['', 'Windows', 'WEB']

def changeState(el, state):
    if isinstance(el, tk.Checkbutton):
        el.configure(state=state)
    else:
        el.nametowidget(el.winfo_parent()).children['!label'].configure(state=state)
        el.configure(state=state)

def changeStates(els, state):
    for el in els.keys():
        changeState(els[el], state)

def versionChange(*args):
    if shared_els_vars['version'].get() == '':
        changeState(shared_els['clients'], tk.DISABLED)
        changeStates(r2_els, tk.DISABLED)
        changeStates(rtc_els, tk.DISABLED)
    elif shared_els_vars['version'].get() == '2009R2':
        changeState(shared_els['clients'], tk.DISABLED)
        changeStates(r2_els, tk.NORMAL)
        changeStates(rtc_els, tk.DISABLED)
    else:
        changeState(shared_els['clients'], tk.NORMAL)
        changeStates(r2_els, tk.DISABLED)
        changeStates(rtc_els, tk.NORMAL)
        changeState(rtc_els['profile_name'], tk.DISABLED)

def useProfile(*args):
    if rtc_els_vars['use_profile'].get() == 1:
        changeState(rtc_els['profile_name'], tk.NORMAL)
    else:
        changeState(rtc_els['profile_name'], tk.DISABLED)

def createConfigure(*args):
    pass

def reqAuth(*args):
    pass

form_els = {}
form_vars = {}

# Shared options
frame_shared = sc_utils.createFormFrame(form_frame, 'Shared', 0, 0)
shared_els = {}
shared_els_vars = {}
shared_data = [
    { 'type': 'entry', 'title': 'System Name', 'col': 0, 'row': 0, 'var_name': 'sys_name', 'opts': '', 'state': tk.NORMAL },
    { 'type': 'option', 'title': 'Navision Version', 'col': 0, 'row': 1, 'var_name': 'version', 'opts': nav_versions, 'state': tk.NORMAL },
    { 'type': 'option', 'title': 'Client', 'col': 0, 'row': 2, 'var_name': 'clients', 'opts': nav_clients, 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'SQL Server', 'col': 0, 'row': 3, 'var_name': 'sql_server', 'opts': '', 'state': tk.NORMAL }
]
sc_utils.createFormSection(form_frame, lbl_font, entry_font, shared_els_vars, shared_els_vars, shared_data)
shared_els_vars['version'].trace('w', versionChange)
# sc_utils.createFormEntry(frame_shared, 'System Name', 0, 0, lbl_font, entry_font, shared_els, shared_els_vars, 'sys_name')
# sc_utils.createOptionMenu(frame_shared, 'Navision Version', nav_versions, 0, 1, lbl_font, entry_font, shared_els, shared_els_vars, 'version')
# shared_els_vars['version'].trace('w', versionChange)
# sc_utils.createOptionMenu(frame_shared, 'Client', nav_clients, 0, 2, lbl_font, entry_font, shared_els, shared_els_vars, 'clients', tk.DISABLED)
# sc_utils.createFormEntry(frame_shared, 'SQL Server', 0, 3, lbl_font, entry_font, shared_els, shared_els_vars, 'sql_server')
# RTC Options
frame_rtc = sc_utils.createFormFrame(form_frame, 'RTC Options', 0, 1)
rtc_els = {}
rtc_els_vars = {}
sc_utils.createFormEntry(frame_rtc, 'RTC Server', 0, 0, lbl_font, entry_font, rtc_els, rtc_els_vars, 'rtc_server', tk.DISABLED)
sc_utils.createFormEntry(frame_rtc, 'Client Services Port', 0, 1, lbl_font, entry_font, rtc_els, rtc_els_vars, 'port', tk.DISABLED)
sc_utils.createFormEntry(frame_rtc, 'Server Instance Name', 0, 2, lbl_font, entry_font, rtc_els, rtc_els_vars, 'instance', tk.DISABLED)
sc_utils.createCheckbox(frame_rtc, 'Use Profile', 0, 3, lbl_font, rtc_els, rtc_els_vars, 'use_profile', tk.DISABLED)
rtc_els_vars['use_profile'].trace('w', useProfile)
sc_utils.createFormEntry(frame_rtc, 'Profile Name', 0, 4, lbl_font, entry_font, rtc_els, rtc_els_vars, 'profile_name', tk.DISABLED)
sc_utils.createCheckbox(frame_rtc, 'Create Configuration Shortcut', 0, 5, lbl_font, rtc_els, rtc_els_vars, 'configure', tk.DISABLED)
rtc_els_vars['configure'].trace('w', createConfigure)
# 2009R2 Options
frame_2009R2 = sc_utils.createFormFrame(form_frame, '2009R2 Options', 0, 2)
r2_els = {}
r2_els_vars = {}
sc_utils.createFormEntry(frame_2009R2, 'Database Name', 0, 0, lbl_font, entry_font, r2_els, r2_els_vars, 'db_name', tk.DISABLED)
sc_utils.createFormEntry(frame_2009R2, 'Company Name', 0, 1, lbl_font, entry_font, r2_els, r2_els_vars, 'company', tk.DISABLED)
sc_utils.createCheckbox(frame_2009R2, 'Require Authentication', 0, 2, lbl_font, r2_els, r2_els_vars, 'req_auth', tk.DISABLED)
r2_els_vars['req_auth'].trace('w', reqAuth)

form_els['shared'] = shared_els
form_els['rtc'] = rtc_els
form_els['r2'] = r2_els
form_vars['shared'] = shared_els_vars
form_vars['rtc'] = rtc_els_vars
form_vars['r2'] = r2_els_vars

form_frame.keys().append('els')
form_frame.keys().append('vars')
form_frame.els = form_els
form_frame.vars = form_vars

# Buttons
# def printData():
#     print(sys_name.get())
# frame_buttons = sc_utils.createFormFrame(form_frame, 'Buttons', 0, 3)
# btn = tk.Button(frame_buttons, text='Test', command=printData)
# btn.grid(column=0, row=0)


icon_size = 75
icon_paths = paths.iconPathsSize(icon_size, paths.icons_path_png)

frame_shortcuts = tk.Frame(window, bd=1, relief=tk.RIDGE)
frame_shortcuts.grid(column=1, row=0)

clr_header_shared = 'gray90'
clr_header_rtc = 'AntiqueWhite1'
clr_header_2009R2 = 'mint cream'#'PaleTurquoise1'
clr_row = 'gray99'

headers = [
    { 'name': 'System Name', 'width': 20, 'clr': clr_header_shared },
    { 'name': 'Client', 'width': 15, 'clr': clr_header_shared },
    { 'name': 'Navision Version', 'width': 15, 'clr': clr_header_shared },
    { 'name': 'SQL Server', 'width': 15, 'clr': clr_header_shared },
    { 'name': 'RTC Server', 'width': 15, 'clr': clr_header_rtc },
    { 'name': 'Services Port', 'width': 15, 'clr': clr_header_rtc },
    { 'name': 'Instance Name', 'width': 15, 'clr': clr_header_rtc },
    { 'name': 'Profile Name', 'width': 25, 'clr': clr_header_rtc },
    { 'name': 'Configuration', 'width': 15, 'clr': clr_header_rtc },
    { 'name': 'Database Name', 'width': 15, 'clr': clr_header_2009R2 },
    { 'name': 'Company', 'width': 15, 'clr': clr_header_2009R2 },
    { 'name': 'Require Authentication', 'width': 20, 'clr': clr_header_2009R2 }
]

icons = []
c = 0
r = 0
stack = 10
cur_system = ''
for i, s in enumerate(systems):
    if cur_system != s['SystemName']:
        cur_system = s['SystemName']
        frame_headers = tk.Frame(frame_shortcuts)
        frame_headers.grid(column=0, row=r)
        r+=1
        for f, h in enumerate(headers):
            sc_utils.createHeader(frame_headers, h['name'], h['width'], h['clr'], f, 0)
    for c, k in enumerate(s.keys()):
        sc_utils.createCell(frame_headers, s[k], headers[c]['width'], clr_row, c, r)
    r+=1
    # c = i % stack
    # if i > 0 and i % stack == 0:
    #     r+=1
    # sc_utils.createIconFrame(frame_shortcuts, system, icons, icon_paths, c, r)

window.mainloop()