import tkinter as tk
import os
import json

icon_size = 75
icon_2009R2 = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_2009R2_{icon_size}.png')
icon_windows = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_windows_{icon_size}.png')
icon_web = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_web_{icon_size}.png')

with open('systems.json') as data:
    systems = json.load(data)

def test_press(event):
    print('label single click')

def test_press2(event):
    print('label double clicked')

window = tk.Tk()

window.title('Navision Shortcuts Manager')

window.geometry('800x600')

frame = tk.Frame(window, relief=tk.RIDGE, padx=0, pady=5, bd=1)
frame.grid(column=0, row=0, padx=2, pady=2)
frame.bind('<Button>', test_press)
frame.bind('<Double-Button-1>', test_press2)

img = tk.PhotoImage(file=icon_2009R2)
icon_lbl = tk.Label(frame, image=img)
# icon_lbl.bind('<Button>', test_press)
# icon_lbl.bind('<Double-Button-1>', test_press2)
icon_lbl.grid(column=0, row=0, padx=10, pady=5)

text_lbl = tk.Label(frame, text='200R2 System')
text_lbl.grid(column=0, row=1)

window.mainloop()