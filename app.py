## Imports ##
import tkinter as tk
from tkinter import ttk
import random
import sqlite3
import pyperclip


## Colors ##
white = "#FFFFFF"
black = "#000000"
darkgray = "#222222"
darkergray = "#363636"
gray = "#3D3D3D"

LARGEFONT = ("Helvetica", 35)
'''
def passwordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
'''

class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FrontPage, Generator, AddElement):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showFrame(FrontPage)
    
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class FrontPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)
        
        label = tk.Label(self, text="Password Manager", font=LARGEFONT, foreground=white, background=gray)
        #label.grid(row=0, column=4, padx=10, pady=10)
        label.place(relx=0.5, rely=0.1, anchor="n")

        #style = ttk.Style()
        #style.configure("W.TButton", font=('calibri', 10, 'bold', 'underline'), background='red')

        button1 = tk.Button(self, text="Generator", font=('Helvetica', 18, 'bold'), bg=darkergray, fg=white, command=lambda:controller.showFrame(Generator))
        button1.place(relx=0.5, rely=0.78, anchor="center", width=300, height=50)

        button2 = tk.Button(self, text="Add Element", font=('Helvetica', 18, 'bold'), bg=darkergray, fg=white, command=lambda:controller.showFrame(AddElement))
        button2.place(relx=0.5, rely=0.85, anchor="center", width=300, height=50)

        search_entry = tk.Entry(self, font=("Helvetica", 18))
        search_entry.place(relx=0.57, rely=0.6, anchor="e", width=200, height=50)

        search_button = tk.Button(self, text="Search", font=('Helvetica', 18, 'bold'), bg=darkergray, fg=white)
        search_button.place(relx=0.57, rely=0.6, anchor="w", width=100, height=50)



class Generator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)

        label = ttk.Label(self, text="Generator", font=LARGEFONT, foreground=white, background=gray)
        label.grid(row=0, column=4, padx=10, pady=10)

        button = ttk.Button(self, text="Front Page",
        command = lambda : controller.showFrame(FrontPage))
        
        button.grid(row=1, column=1, padx=10, pady=10)

class AddElement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)

        label = ttk.Label(self, text="Add Element", font=LARGEFONT, foreground=white, background=gray)
        label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Front Page", command = lambda : controller.showFrame(FrontPage))
        button.grid(row=1, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Website", font=LARGEFONT, foreground=white, background=gray)
        label.place(x=175, y=75)

        search_entry = tk.Entry(self, font=("Helvetica", 18))
        search_entry.place(x=360, y=150, anchor="e", width=200, height=25)


        label = ttk.Label(self, text="Email", font=LARGEFONT, foreground=white, background=gray)
        label.place(x=175, y=180 )

        search_entry = tk.Entry(self, font=("Helvetica", 18))
        search_entry.place(x=360, y=250, anchor="e", width=200, height=25)


        label = ttk.Label(self, text="Password", font=LARGEFONT, foreground=white, background=gray)
        label.place(x=175, y=275)

        search_entry = tk.Entry(self, font=("Helvetica", 18))
        search_entry.place(x=360, y=350, anchor="e", width=200, height=25)

        button = tk.Button(self, text="ADD", command = lambda : controller.showFrame(FrontPage))
        button.place(x=600, y=600)


screen = TkinterApp()
screen.geometry("700x750")
screen.resizable(False,False)
screen.title("Password Manager")
icon = tk.PhotoImage(file='assets\icon.png')
screen.wm_iconphoto(False, icon)

screen.mainloop()
