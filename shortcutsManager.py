import tkinter as tk
import paths
import shortcutUtils as sc_utils
import miscData as misc_data

systems = sc_utils.parseSystemsJSON('systems.json')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('1680x960')

form_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
form_frame.grid(column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='NESW')

form_els = {}
form_vars = {}

# Shared options
shared_els, shared_els_vars = sc_utils.createFormSection(form_frame, 'Shared', 0, 0, misc_data.lbl_font, misc_data.entry_font, misc_data.shared_data)
# RTC Options
rtc_els, rtc_els_vars = sc_utils.createFormSection(form_frame, 'RTC Options', 0, 1, misc_data.lbl_font, misc_data.entry_font, misc_data.rtc_data)
# 2009R2 Options
r2_els, r2_els_vars = sc_utils.createFormSection(form_frame, '2009R2 Options', 0, 2, misc_data.lbl_font, misc_data.entry_font, misc_data.r2_data)

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

shared_els_vars['version'].trace('w', lambda *args: sc_utils.versionChange(form_els=form_els, form_vars=form_vars))
rtc_els_vars['use_profile'].trace('w', lambda *args: sc_utils.useProfile(rtc_els=rtc_els, rtc_vars=rtc_els_vars))
rtc_els_vars['configure'].trace('w', sc_utils.createConfigure)
r2_els_vars['req_auth'].trace('w', sc_utils.reqAuth)

icon_size = 75
icon_paths = paths.iconPathsSize(icon_size, paths.icons_path_png)

frame_shortcuts = tk.Frame(window, bd=1, relief=tk.RIDGE)
frame_shortcuts.grid(column=1, row=0)

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
        for f, h in enumerate(misc_data.headers):
            sc_utils.createHeader(frame_headers, h['name'], h['width'], h['clr'], f, 0)
    for c, k in enumerate(s.keys()):
        sc_utils.createCell(frame_headers, s[k], misc_data.headers[c]['width'], misc_data.clr_row, c, r)
    r+=1
    # c = i % stack
    # if i > 0 and i % stack == 0:
    #     r+=1
    # sc_utils.createIconFrame(frame_shortcuts, system, icons, icon_paths, c, r)

window.mainloop()