## Imports ##
import tkinter as tk
from tkinter import ttk
import secrets
import string
import sqlite3
import pyperclip


## Colors ##
white = "#FFFFFF"
black = "#000000"
darkgray = "#222222"
darkergray = "#363636"
gray = "#3D3D3D"

LARGEFONT = ("Helvetica", 35)

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

        back_button = ttk.Button(self, text="Front Page", command=lambda:controller.showFrame(FrontPage))
        back_button.grid(row=1, column=1, padx=10, pady=10)

        generate_button = tk.Button(self, text="Generate", font=('Helvetica', 18, 'bold'), bg=darkergray, fg=white, command=self.passwordGenerator)
        generate_button.place(relx=0.5, rely=0.6, anchor="s", width=300, height=50)

        self.thicc_check = tk.BooleanVar()
        thicc_checkbox = tk.Checkbutton(self, text="A-Z", variable=self.thicc_check)
        thicc_checkbox.place(relx=0.4, rely=0.5)

        self.numbers_check = tk.BooleanVar()
        numbers_checkbox = tk.Checkbutton(self, text="0-9", variable=self.numbers_check)
        numbers_checkbox.place(relx=0.4, rely=0.6)

        self.symbols_check = tk.BooleanVar()
        symbols_checkbox = tk.Checkbutton(self, text="!@#$%^&*", variable=self.symbols_check)
        symbols_checkbox.place(relx=0.4, rely=0.7)

        self.length_var = tk.IntVar()
        length_scale = tk.Scale(self, from_=1, to=100, orient='horizontal', variable=self.length_var)
        length_scale.place(relx=0.4, rely=0.8)

        self.entry = tk.Text(self)
        self.entry.place(x=100, y=100, width=200, height=50)
    
    def passwordGenerator(self):
        length = self.length_var.get()
        thicc_check = self.thicc_check.get()
        numbers_check = self.numbers_check.get()
        symbols_check = self.symbols_check.get()

        smol_letters = string.ascii_lowercase

        if thicc_check == True:
            thicc_letters = string.ascii_uppercase
        else:
            thicc_letters = ""

        if numbers_check == True:
            numbers = string.digits
        else:
            numbers = ""

        if symbols_check == True:
            symbols = string.punctuation
        else:
            symbols = ""

        all = smol_letters + thicc_letters + numbers + symbols

        password = ""
        for i in range(length):
            password += "".join(secrets.choice(all))

        self.entry.configure(state='normal')
        self.entry.delete(1.0, 'end')
        self.entry.insert('end', password)
        self.entry.configure(state='disabled')

        print(password)
        pyperclip.copy(password)


class AddElement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)

        label = ttk.Label(self, text="Add Element", font=LARGEFONT, foreground=white, background=gray)
        label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Front Page", command=lambda:controller.showFrame(FrontPage))
        button.grid(row=1, column=1, padx=10, pady=10)

screen = TkinterApp()
screen.geometry("700x750")
screen.resizable(False, False)
screen.title("Password Manager")
icon = tk.PhotoImage(file='assets\icon.png')
screen.wm_iconphoto(False, icon)

screen.mainloop()
