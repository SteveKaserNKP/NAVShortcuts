import os

# DIRECTORIES
directory = os.path.dirname(__file__)

shortcuts_path = os.path.join(directory, 'test')
configs_path = os.path.join(directory, 'testConfig')
icons_path_ico = os.path.join(directory, 'icons', 'ico')
icons_path_png = os.path.join(directory, 'icons', 'png')

def iconPathsSize(icon_size, icons_path):
    icons = {}
    icons['icon_2009R2'] = os.path.join(icons_path, f'icon_2009R2_{icon_size}.png')
    icons['icon_windows'] = os.path.join(icons_path, f'icon_windows_{icon_size}.png')
    icons['icon_web'] = os.path.join(icons_path, f'icon_web_{icon_size}.png')
    return icons

# PROGRAMS
nav_folder = os.path.join("C:/","Program Files (x86)","Microsoft Dynamics NAV")
rtc_exe = os.path.join("RoleTailored Client","Microsoft.Dynamics.Nav.Client.exe")
exe_ie = os.path.join("C:/", "Program Files", "Internet Explorer", "iexplore.exe")

exe_2009R2 = os.path.join(nav_folder,"60","Classic","finsql.exe")
exe_2016 = os.path.join(nav_folder,"90",rtc_exe)
exe_2017 = os.path.join(nav_folder,"100",rtc_exe)
exe_2018 = os.path.join(nav_folder,"110",rtc_exe)