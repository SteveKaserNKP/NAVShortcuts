import tkinter as tk

lbl_font = ('Calibri', 12)
entry_font = ('Ebrima', 14)

nav_versions = ['', '2009R2', '2016', '2017', '2018']
nav_clients = ['', 'Windows', 'WEB']

shared_data = [
    { 'type': 'entry', 'title': 'System Name', 'col': 0, 'row': 0, 'var_name': 'sys_name', 'opts': {}, 'state': tk.NORMAL },
    { 'type': 'option', 'title': 'Navision Version', 'col': 0, 'row': 1, 'var_name': 'version', 'opts': nav_versions, 'state': tk.NORMAL },
    { 'type': 'option', 'title': 'Client', 'col': 0, 'row': 2, 'var_name': 'clients', 'opts': nav_clients, 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'SQL Server', 'col': 0, 'row': 3, 'var_name': 'sql_server', 'opts': {}, 'state': tk.NORMAL }
]

rtc_data = [
    { 'type': 'entry', 'title': 'RTC Server', 'col': 0, 'row': 0, 'var_name': 'rtc_server', 'opts': {}, 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'Client Services Port', 'col': 0, 'row': 2, 'var_name': 'port', 'opts': {}, 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'Server Instance Name', 'col': 0, 'row': 3, 'var_name': 'instance', 'opts': {}, 'state': tk.DISABLED },
    { 'type': 'check', 'title': 'Use Profile', 'col': 0, 'row': 4, 'var_name': 'use_profile', 'opts': {}, 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'Profile Name', 'col': 0, 'row': 5, 'var_name': 'profile_name', 'opts': {}, 'state': tk.DISABLED },
    { 'type': 'check', 'title': 'Create Configuration Shortcut', 'col': 0, 'row': 6, 'var_name': 'configure', 'opts': {}, 'state': tk.DISABLED },
]

r2_data = [
    { 'type': 'entry', 'title': 'Database Name', 'col': 0, 'row': 0, 'var_name': 'db_name', 'state': tk.DISABLED },
    { 'type': 'entry', 'title': 'Company', 'col': 0, 'row': 1, 'var_name': 'company', 'state': tk.DISABLED },
    { 'type': 'check', 'title': 'Require Authentication', 'col': 0, 'row': 2, 'var_name': 'req_auth', 'state': tk.DISABLED },
]

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