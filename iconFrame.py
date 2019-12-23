class IconFrame:
    def __init__(self, tk, master, data):
        self.tk = tk
        self.master = master
        self.data = data

    def create(self):
        self.frame = self.tk.Frame(self.master, relief=self.tk.RIDGE, padx=0, pady=5, bd=1)
        self.frame.bind('<Double-Button-1>', self.doubleClick)
        # self.frame.setvar('data', self.data)
        return self.frame

    def grid(self, c, r):
        pass

    def doubleClick(self, event):
        # d = event.widget.getvar('data')
        print(f'from frame: {self.data}')