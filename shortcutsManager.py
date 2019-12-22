from tkinter import *

def test_press(event):
    print('label single clicked')

def test_press2(event):
    print('label double clicked')

window = Tk()

window.title('Navision Shortcuts Manager')

window.geometry('800x600')

test_lbl = Label(window, text='2018 Systems')

test_lbl.grid(column=0, row=0)

test_lbl.bind('<Button>', test_press)
test_lbl.bind('<Double-Button-1>', test_press2)

window.mainloop()