import tkinter as tk
import paths
import shortcutUtils as sc_utils
import miscData as misc_data

systems = sc_utils.parseSystemsJSON('systems.json')

window = tk.Tk()
window.title('Navision Shortcuts Manager')
window.geometry('1680x960')

# form_frame = tk.Frame(window, bd=1, relief=tk.RIDGE)
# form_frame.grid(column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='NS')

# form_els = {}
# form_vars = {}

# # Shared options
# shared_els, shared_els_vars = sc_utils.createFormSection(form_frame, 'Shared', 0, 0, misc_data.lbl_font, misc_data.entry_font, misc_data.shared_data)
# # RTC Options
# rtc_els, rtc_els_vars = sc_utils.createFormSection(form_frame, 'RTC Options', 0, 1, misc_data.lbl_font, misc_data.entry_font, misc_data.rtc_data)
# # 2009R2 Options
# r2_els, r2_els_vars = sc_utils.createFormSection(form_frame, '2009R2 Options', 0, 2, misc_data.lbl_font, misc_data.entry_font, misc_data.r2_data)

# form_els['shared'] = shared_els
# form_els['rtc'] = rtc_els
# form_els['r2'] = r2_els
# form_vars['shared'] = shared_els_vars
# form_vars['rtc'] = rtc_els_vars
# form_vars['r2'] = r2_els_vars

# form_frame.keys().append('els')
# form_frame.keys().append('vars')
# form_frame.els = form_els
# form_frame.vars = form_vars

# shared_els_vars['version'].trace('w', lambda *args: sc_utils.versionChange(form_els=form_els, form_vars=form_vars))
# rtc_els_vars['use_profile'].trace('w', lambda *args: sc_utils.useProfile(rtc_els=rtc_els, rtc_vars=rtc_els_vars))
# rtc_els_vars['configure'].trace('w', sc_utils.createConfigure)
# r2_els_vars['req_auth'].trace('w', sc_utils.reqAuth)

def setSelection(widget):
    parentName = widget.winfo_parent()
    parent = widget._nametowidget(parentName)
    if widget in parent.selected:
        parent.selected.remove(widget)
        widget.configure(relief=tk.RIDGE, bg='SystemButtonFace')
    else:
        parent.selected.append(widget)
        widget.configure(relief=tk.SUNKEN, bg='SeaGreen1')

# def setSelections(frame, items):
#     selected_frame_widgets = {frame.children[w] for w in frame.children.keys() if frame.children[w] in frame.selected}
#     needs_unset = items & selected_frame_widgets
#     if needs_unset:
#         list(map(lambda  w: setSelection(w), needs_unset))
#     needs_set = items - selected_frame_widgets
#     list(map(lambda  w: setSelection(w), needs_set))

def selectSystem(event):
    setSelection(event.widget)
    parentName = event.widget.winfo_parent()
    parent = event.widget._nametowidget(parentName)
    selected_systems = sorted([sys.cget('text') for sys in parent.selected])
    sys_obj_list = [sys for sys in systems if sys['SystemName'] in selected_systems]
    sys_name_tuple = sorted({sys['SystemName'] for sys in sys_obj_list})
    sys_dict = {}
    for sys in sys_name_tuple:
        sys_dict[sys] = [so for so in sys_obj_list if so['SystemName'] == sys]
    for s in frame_shortcuts.grid_slaves():
        s.destroy()
    createShortcutsList(sys_dict, frame_shortcuts, 0)
    # versions = {sys['NavisionVersion'] for sys in systems if sys['SystemName'] == event.widget.cget('text')}
    # frame = frames['versions']
    # version_widgets = { frame.children[w] for w in frame.children.keys() if frame.children[w].cget('text') in versions }
    # setSelections(frames['versions'], version_widgets)

def selectVersion(event):
    setSelection(event.widget)

def selectClient(event):
    setSelection(event.widget)

def selectSQLServer(event):
    setSelection(event.widget)

def createShortcutsList(systems_list, shortcuts_frame, r):
    for sys in systems_list.values():
        frame_headers = tk.Frame(shortcuts_frame)
        frame_headers.grid(column=0, row=r)
        for f, h in enumerate(misc_data.headers):
            sc_utils.createHeader(frame_headers, h['name'], h['width'], h['clr'], f, r)
        r+=1
        for s in sys:
            frame_row = tk.Frame(frame_headers)
            frame_row.grid(column=0, row=r)
            for c, k in enumerate(s.keys()):
                sc_utils.createCell(frame_row, s[k], misc_data.headers[c]['width'], misc_data.clr_row, c, r)
            r+=1

icon_size = 75
icon_paths = paths.iconPathsSize(icon_size, paths.icons_path_png)

frame_buttons = tk.Frame(window, bd=1, relief=tk.RIDGE)
frame_buttons.grid(column=1, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky='W')
frame_shortcuts = tk.Frame(window, bd=1, relief=tk.RIDGE)
frame_shortcuts.grid(column=1, row=1, ipadx=5, ipady=5, padx=5, pady=5, sticky='W')

def createButtonFrame(master, form_name, c, r):
    frame_btns = sc_utils.createFormFrame(master, form_name, c, r)
    frame_btns.keys().append('selected')
    frame_btns.selected = []
    return frame_btns

def insertLabelButtons(master, items, stack, lbl_name, lbl_width, callback):
    r = 0
    for i, s in enumerate(items):
        lbl = tk.Label(master, text=s, width=lbl_width, bd=1, relief=tk.RIDGE, padx=5, pady=5)
        lbl.keys().append(lbl_name)
        lbl.setvar(lbl_name, s)
        lbl.bind('<Button-1>', callback)
        if i > 0 and i % stack == 0:
            r+=1
        lbl.grid(column=i%stack, row=r)

sys_names = sorted({sys['SystemName'] for sys in systems})
sql_servers = sorted({sys['SQLServer'] for sys in systems})
stack = 6
button_frames = {
    'systems': createButtonFrame(frame_buttons, 'Systems', 0, 0),
    'versions': createButtonFrame(frame_buttons, 'Versions', 0, 1),
    'clients': createButtonFrame(frame_buttons, 'Clients', 0, 2),
    'sql_servers': createButtonFrame(frame_buttons, 'SQL Servers', 0, 3)
}
# insertLabelButtons(button_frames['systems'], sys_names, stack, 'system', 15, lambda event: selectSystem(event, frames=button_frames))
insertLabelButtons(button_frames['systems'], sys_names, stack, 'system', 15, selectSystem)
insertLabelButtons(button_frames['versions'], misc_data.nav_versions[1:], stack, 'version', 15, selectVersion)
insertLabelButtons(button_frames['clients'], misc_data.nav_clients[1:], stack, 'client', 15, selectClient)
insertLabelButtons(button_frames['sql_servers'], sql_servers, stack, 'sql_server', 15, selectSQLServer)

# icons = []
# c = 0
# cur_system = ''
    ### USED FOR CREATING ICONLABELS - old
    # r+=1
    # c = i % stack
    # if i > 0 and i % stack == 0:
    #     r+=1
    # sc_utils.createIconFrame(frame_shortcuts, system, icons, icon_paths, c, r)

window.mainloop()