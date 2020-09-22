import tkinter as tk


class GUI:
    def __init__(self):
        pass

    def gui(self):
        window = tk.Tk()
        greeting = tk.Label(text='Hello, World').pack()
        window.mainloop()