import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.ww = 0
        self.root = tk.Tk()
        self.root.title("Tysiąc")
        self.root.geometry("550x500")
        self.root.configure(bg='beige')
        self.label = tk.Label(self.root, text="Tysiąc", font=('Impact', 32), bg='beige')
        self.label.pack(padx = 10, pady = 30)
        self.wynik = tk.Label(self.root, text="0", font=('Calibri', 36), bg='beige')
        self.wynik.pack(padx=10, pady=30)
        # self.textbox = tk.Text(self.root, height = 4, font=("Calibri", 16))
        # self.textbox.place(x = 25, y = 100, height = 130, width = 500)
        # self.select = tk.Button(self.root, text="Wybierz metodę", font=('Calibri', 24), command=self.select)
        # self.select.place(x = 1000, y = 200, height = 50, width = 250)
        self.aceb = tk.Button(self.root, text = "A", font = ('Calibri', 18), command=self.ace)
        self.aceb.place(x = 50, y = 400, height = 50, width = 50)
        self.tenb = tk.Button(self.root, text = "10", font = ('Calibri', 18), command=self.ten)
        self.tenb.place(x = 150, y = 400, height = 50, width = 50)
        self.kingb = tk.Button(self.root, text = "K", font = ('Calibri', 18), command=self.king)
        self.kingb.place(x = 250, y = 400, height = 50, width = 50)
        self.queenb = tk.Button(self.root, text = "Q", font = ('Calibri', 18), command=self.queen)
        self.queenb.place(x = 350, y = 400, height = 50, width = 50)
        self.jackb = tk.Button(self.root, text = "J", font = ('Calibri', 18), command=self.jack)
        self.jackb.place(x = 450, y = 400, height = 50, width = 50)
        self.clearb = tk.Button(self.root, text = "Clear", font = ('Calibri', 18), command=self.clear)
        self.clearb.place(x=205, y=300, height=50, width=150)
        # self.anwser = tk.Label(self.root, wraplength=600, text=None, font=('Impact', 24), bg='beige')
        # self.anwser.place(x = 150, y = 400)
        # self.info = tk.Button(self.root, text = "Jak to działa?", font = ('Calibri', 24, "bold"), command = self.help)
        # self.info.place(x = 25, y = 25, height = 50, width = 250)
        # self.export = tk.Button(self.root, text="Eksportować w PDF", font=('Calibri', 24), command=self.pdf)
        # self.export.place(x = 950, y = 630, height = 65, width = 300)
        # self.options = ["Caesar Cipher", "Transposition Cipher", "Cyrillic Cipher"]
        # self.clicked = tk.StringVar()
        self.root.bind("1", self.ace)
        self.root.bind("2", self.ten)
        self.root.bind("3", self.king)
        self.root.bind("4", self.queen)
        self.root.bind("5", self.jack)
        self.root.bind("<space>", self.clear)
        self.root.mainloop()
    def ace(self, event=None):
        # print(11)
        self.ww += 11
        self.wynik.config(text=self.ww)
        pass
    def ten(self, event=None):
        self.ww += 10
        self.wynik.config(text=self.ww)
    def king(self, event=None):
        self.ww += 4
        self.wynik.config(text=self.ww)
    def queen(self, event=None):
        self.ww += 3
        self.wynik.config(text=self.ww)
    def jack(self, event=None):
        self.ww += 2
        self.wynik.config(text=self.ww)
    def clear(self, event=None):
        self.ww = 0
        self.wynik.config(text=self.ww)
gui=GUI()
