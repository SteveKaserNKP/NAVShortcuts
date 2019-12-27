import tkinter as tk
import paths
import shortcutUtils as sc_utils

systems = sc_utils.parseSystemsJSON('systems.json')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('1680x960')

form_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
form_frame.widgetName = 'formFrame'
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
    if version.get() == '':
        changeState(shared_els['clients'], tk.DISABLED)
        changeStates(r2_els, tk.DISABLED)
        changeStates(rtc_els, tk.DISABLED)
    elif version.get() == '2009R2':
        changeState(shared_els['clients'], tk.DISABLED)
        changeStates(r2_els, tk.NORMAL)
        changeStates(rtc_els, tk.DISABLED)
    else:
        changeState(shared_els['clients'], tk.NORMAL)
        changeStates(r2_els, tk.DISABLED)
        changeStates(rtc_els, tk.NORMAL)
        changeState(rtc_els['profile_name'], tk.DISABLED)

def useProfile(*args):
    if use_profile_var.get() == 1:
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
sys_name, sys_name_var = sc_utils.createFormEntry(frame_shared, 'System Name', 0, 0, lbl_font, entry_font)
shared_els['sys_name'] = sys_name
shared_els_vars['sys_name'] = sys_name_var
versions, version = sc_utils.createOptionMenu(frame_shared, 'Navision Version', nav_versions, 0, 1, lbl_font, entry_font)
shared_els['versions'] = versions
shared_els_vars['version'] = version
shared_els_vars['version'].trace('w', versionChange)
clients, client = sc_utils.createOptionMenu(frame_shared, 'Client', nav_clients, 0, 2, lbl_font, entry_font, tk.DISABLED)
shared_els['clients'] = clients
shared_els_vars['client'] = client
sql_server, sql_server_var = sc_utils.createFormEntry(frame_shared, 'SQL Server', 0, 3, lbl_font, entry_font)
shared_els['sql_server'] = sql_server
shared_els_vars['sql_server'] = sql_server_var
# RTC Options
frame_rtc = sc_utils.createFormFrame(form_frame, 'RTC Options', 0, 1)
rtc_els = {}
rtc_els_vars = {}
rtc_server, rtc_server_var = sc_utils.createFormEntry(frame_rtc, 'RTC Server', 0, 0, lbl_font, entry_font, tk.DISABLED)
rtc_els['rtc_server'] = rtc_server
rtc_els_vars['rtc_server'] = rtc_server_var
port, port_var = sc_utils.createFormEntry(frame_rtc, 'Client Services Port', 0, 1, lbl_font, entry_font, tk.DISABLED)
rtc_els['port'] = port
rtc_els_vars['port'] = port_var
instance, instance_var = sc_utils.createFormEntry(frame_rtc, 'Server Instance Name', 0, 2, lbl_font, entry_font, tk.DISABLED)
rtc_els['instance'] = instance
rtc_els_vars['instance'] = instance_var
use_profile, use_profile_var = sc_utils.createCheckbox(frame_rtc, 'Use Profile', 0, 3, lbl_font, tk.DISABLED)
rtc_els['use_profile'] = use_profile
rtc_els_vars['use_profile'] = use_profile_var
rtc_els_vars['use_profile'].trace('w', useProfile)
profile_name, profile_name_var = sc_utils.createFormEntry(frame_rtc, 'Profile Name', 0, 4, lbl_font, entry_font, tk.DISABLED)
rtc_els['profile_name'] = profile_name
rtc_els_vars['profile_name'] = profile_name_var
configure, configure_var = sc_utils.createCheckbox(frame_rtc, 'Create Configuration Shortcut', 0, 5, lbl_font, tk.DISABLED)
rtc_els['configure'] = configure
rtc_els_vars['configure'] = configure_var
rtc_els_vars['configure'].trace('w', createConfigure)
# 2009R2 Options
frame_2009R2 = sc_utils.createFormFrame(form_frame, '2009R2 Options', 0, 2)
r2_els = {}
r2_els_vars = {}
db_name, db_name_var = sc_utils.createFormEntry(frame_2009R2, 'Database Name', 0, 0, lbl_font, entry_font, tk.DISABLED)
r2_els['db_name'] = db_name
r2_els_vars['db_name'] = db_name_var
company, company_var = sc_utils.createFormEntry(frame_2009R2, 'Company Name', 0, 1, lbl_font, entry_font, tk.DISABLED)
r2_els['company'] = company
r2_els_vars['company'] = company_var
req_auth, req_auth_var = sc_utils.createCheckbox(frame_2009R2, 'Require Authentication', 0, 2, lbl_font, tk.DISABLED)
r2_els['req_auth'] = req_auth
r2_els_vars['req_auth'] = req_auth_var
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
frame_shortcuts.grid(column=1, row=0, padx=5, pady=5, sticky='EW')

frame_headers = tk.Frame(frame_shortcuts)
frame_headers.grid(column=1, row=0)

clr_header = 'aquamarine'
clr_row = 'mint cream'

lbl_sys_name = tk.Label(frame_headers, text='System Name', bd=1, relief=tk.RIDGE, width=20, bg=clr_header)
lbl_client = tk.Label(frame_headers, text='Client', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_version = tk.Label(frame_headers, text='Navision Version', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_sql_server = tk.Label(frame_headers, text='SQL Server', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_rtc_server = tk.Label(frame_headers, text='RTC Server', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_port = tk.Label(frame_headers, text='Services Port', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_instance = tk.Label(frame_headers, text='Instance Name', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_profile = tk.Label(frame_headers, text='Profile Name', bd=1, relief=tk.RIDGE, width=20, bg=clr_header)
lbl_configure = tk.Label(frame_headers, text='Configuration', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_db_name = tk.Label(frame_headers, text='Database Name', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_company = tk.Label(frame_headers, text='Company', bd=1, relief=tk.RIDGE, width=15, bg=clr_header)
lbl_req_auth = tk.Label(frame_headers, text='Require Authentication', bd=1, relief=tk.RIDGE, width=20, bg=clr_header)

lbl_sys_name.grid(column=0, row=0)
lbl_client.grid(column=1, row=0)
lbl_version.grid(column=2, row=0)
lbl_sql_server.grid(column=3, row=0)
lbl_rtc_server.grid(column=4, row=0)
lbl_port.grid(column=5, row=0)
lbl_instance.grid(column=6, row=0)
lbl_profile.grid(column=7, row=0)
lbl_configure.grid(column=8, row=0)
lbl_db_name.grid(column=9, row=0)
lbl_company.grid(column=10, row=0)
lbl_req_auth.grid(column=11, row=0)

icons = []
c = 0
r = 0
stack = 10
for i, s in enumerate(systems):
    lbl_sys_name2 = tk.Label(frame_headers, text=s['SystemName'], bd=1, relief=tk.FLAT, width=20, bg=clr_row)
    lbl_client2 = tk.Label(frame_headers, text=s['Client'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_version2 = tk.Label(frame_headers, text=s['NavisionVersion'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_sql_server2 = tk.Label(frame_headers, text=s['SQLServer'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_rtc_server2 = tk.Label(frame_headers, text=s['RTCServer'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_port2 = tk.Label(frame_headers, text=s['ClientServicesPort'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_instance2 = tk.Label(frame_headers, text=s['ServerInstanceName'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_profile2 = tk.Label(frame_headers, text=s['Profile'], bd=1, relief=tk.FLAT, width=20, bg=clr_row)
    lbl_configure2 = tk.Label(frame_headers, text=s['Configure'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_db_name2 = tk.Label(frame_headers, text=s['DatabaseName'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_company2 = tk.Label(frame_headers, text=s['Company'], bd=1, relief=tk.FLAT, width=15, bg=clr_row)
    lbl_req_auth2 = tk.Label(frame_headers, text=s['RequireAuthentication'], bd=1, relief=tk.FLAT, width=20, bg=clr_row)

    theRow = i + 1
    lbl_sys_name2.grid(column=0, row=theRow)
    lbl_client2.grid(column=1, row=theRow)
    lbl_version2.grid(column=2, row=theRow)
    lbl_sql_server2.grid(column=3, row=theRow)
    lbl_rtc_server2.grid(column=4, row=theRow)
    lbl_port2.grid(column=5, row=theRow)
    lbl_instance2.grid(column=6, row=theRow)
    lbl_profile2.grid(column=7, row=theRow)
    lbl_configure2.grid(column=8, row=theRow)
    lbl_db_name2.grid(column=9, row=theRow)
    lbl_company2.grid(column=10, row=theRow)
    lbl_req_auth2.grid(column=11, row=theRow)
    # c = i % stack
    # if i > 0 and i % stack == 0:
    #     r+=1
    # sc_utils.createIconFrame(frame_shortcuts, system, icons, icon_paths, c, r)

window.mainloop()