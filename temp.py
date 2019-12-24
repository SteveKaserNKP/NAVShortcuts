### figuring out how to make the frame unique
# import tkinter as tk

# root = tk.Tk()

# def onClick(event):
#     f = event.widget
#     print(f.temp_id)

# for i in range(10):
#     f = tk.Frame(root, padx=50, pady=50, background='grey' if i % 2 == 0 else '')
#     f.bind("<Button-1>", onClick)
#     f.keys().append('temp_id')
#     f.temp_id = i
#     l = tk.Label(f, text=i)
#     l.grid(column=0, row=0)
#     f.grid(column=i,row=0)

# root.mainloop()

### dropdown menu
# from tkinter import *

# master = Tk()

# variable = StringVar(master)
# variable.set("one") # default value

# w = OptionMenu(master, variable, "one", "two", "three")
# w.pack()

# mainloop()