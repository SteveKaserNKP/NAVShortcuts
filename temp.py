import tkinter as tk

root = tk.Tk()
root.minsize(200, 200)

def onClick(event):
    btn = event.widget # event.widget is the widget that called the event
    print(btn.getvar("temp_id")) #Print the text for the selected button

for i in range(10):
    b = tk.Frame(root, relief=tk.RIDGE, padx=0, pady=5, bd=1)
    l = tk.Label(b, text=i)
    l.grid(column=0, row=0)
    b.setvar('temp_id', i)
    b.grid(row = i, column = 0)
    # Bind to left click which generates an event object
    b.bind("<Button-1>", onClick)

root.mainloop()