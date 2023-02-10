## Imports ##
import tkinter as tk
import secrets
import string
import sqlite3
import pyperclip

## Variables ##
# Colors
white = "#FFFFFF"
black = "#000000"
darkgray = "#222222"
darkergray = "#363636"
gray = "#3D3D3D"
lightgray = "#898989"

title_font = ("Helvetica", 35, "bold")
standard_font = ("Helvetica", 18)

button_width = 300
button_height = 50

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
        
        ## GUI ##
        # Font Page Title
        frontPage_title = tk.Label(
            self, 
            text = "Password Manager", 
            font = title_font, 
            foreground = white, 
            background = gray
        )
        frontPage_title.place(relx=0.5, rely=0.1, anchor="center")

        # Generator Button
        generator_button = tk.Button(
            self, 
            text = "Generator", 
            font = standard_font, 
            background = darkergray, 
            foreground = white,
            activebackground = darkgray,
            activeforeground = white,
            command = lambda:controller.showFrame(Generator)
        )
        generator_button.place(relx=0.5, rely=0.78, anchor="center", width=button_width, height=button_height)

        # Add Element Button
        addElement_button = tk.Button(
            self, 
            text = "Add Element", 
            font = standard_font, 
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            command = lambda:controller.showFrame(AddElement)
        )
        addElement_button.place(relx=0.5, rely=0.85, anchor="center", width=button_width, height=button_height)

        # Search Entry Field
        search_entry = tk.Entry(
            self, 
            font = standard_font,
            background = darkergray,
            foreground = white
        )
        search_entry.place(relx=0.43, rely=0.6, anchor="center", width=button_width-100, height=button_height)

        # Search Button
        search_button = tk.Button(
            self, 
            text = "Search", 
            font = standard_font, 
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
        )
        search_button.place(relx=0.64, rely=0.6, anchor="center", width=100, height=50)


class Generator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)

        ## GUI ##
        # Generator Title
        generator_title = tk.Label(
            self, 
            text = "Generator", 
            font = title_font, 
            foreground = white, 
            background = gray
        )
        generator_title.place(relx=0.5, rely=0.1, anchor="center")

        # Back Button
        back_button = tk.Button(
            self, 
            text = "Back", 
            font = standard_font, 
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            command = lambda:controller.showFrame(FrontPage)
        )
        back_button.place(x=0, y=0, anchor="nw", width=100, height=50)

        # Generate Button
        generate_button = tk.Button(
            self, 
            text = "Generate", 
            font = standard_font, 
            background = darkergray, 
            foreground = white,
            activebackground = darkgray,
            activeforeground = white, 
            command = self.passwordGenerator
        )
        generate_button.place(relx=0.5, rely=0.6, anchor="s", width=button_width, height=button_height)

        # Password Text Display
        self.password_display = tk.Text(
            self, 
            font = ("courier", 16), 
            background = darkergray, 
            foreground = white, 
        )
        self.password_display.place(relx=0.5, rely=0.3, anchor="center", width=500, height=75)
        self.password_display.configure(state='disabled')

        # Add Password to Element
        addToElement_button = tk.Button(
            self,
            text = "Add to Element", 
            font = standard_font, 
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
        )
        addToElement_button.place(relx=0.5, rely=0.85, anchor="center", width=button_width, height=button_height)

        # Copy Password Button
        copy_button = tk.Button(
            self, 
            text = "Copy Password", 
            font = standard_font, 
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            command = self.copyPassword
        )
        copy_button.place(relx=0.5, rely=0.78, anchor="center", width=button_width, height=button_height)

        # Uppercase Letters Checkbox
        self.upper_check = tk.BooleanVar()
        upper_checkbox = tk.Checkbutton(
            self, 
            text = "A-Z", 
            font=("Helvetiva", 12),
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            selectcolor = darkergray,
            variable = self.upper_check
        )
        upper_checkbox.place(relx=0.32, rely=0.4, anchor="center")

        # Symbols Checkbox
        self.symbols_check = tk.BooleanVar()
        symbols_checkbox = tk.Checkbutton(
            self, 
            text = "!@#$%^&*",
            font=("Helvetiva", 12),
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            selectcolor = darkergray,
            variable = self.symbols_check
        )
        symbols_checkbox.place(relx=0.5, rely=0.4, anchor="center")

        # Numbers Checkbox
        self.numbers_check = tk.BooleanVar()
        numbers_checkbox = tk.Checkbutton(
            self, 
            text = "0-9",
            font=("Helvetiva", 12),
            background = darkergray, 
            foreground = white, 
            activebackground = darkgray,
            activeforeground = white,
            selectcolor = darkergray,
            variable = self.numbers_check
        )
        numbers_checkbox.place(relx=0.68, rely=0.4, anchor="center")

        # Password Length Scale
        self.length_var = tk.IntVar()
        length_scale = tk.Scale(
            self, 
            background = darkergray, 
            foreground = white,
            activebackground= darkgray,
            troughcolor = darkgray,
            from_ = 1, 
            to = 100, 
            orient = 'horizontal', 
            variable = self.length_var
        )
        length_scale.place(relx=0.5, rely=0.48, anchor="center", width=button_width)
    
    def passwordGenerator(self):
        length = self.length_var.get()
        upper_check = self.upper_check.get()
        numbers_check = self.numbers_check.get()
        symbols_check = self.symbols_check.get()

        lower_letters = string.ascii_lowercase

        if upper_check == True:
            upper_letters = string.ascii_uppercase
        else:
            upper_letters = ""

        if numbers_check == True:
            numbers = string.digits
        else:
            numbers = ""

        if symbols_check == True:
            symbols = string.punctuation
        else:
            symbols = ""

        temp_password = lower_letters + upper_letters + numbers + symbols

        self.password = ""
        for i in range(length):
            self.password += "".join(secrets.choice(temp_password))

        self.password_display.configure(state='normal')
        self.password_display.delete(1.0, 'end')
        self.password_display.insert('end', self.password)
        self.password_display.configure(state='disabled')
    
    def copyPassword(self):
        pyperclip.copy(self.password)


class AddElement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=gray)

        ## GUI ##
        # Add Element Title
        addElement_title = tk.Label(self, text="Add Element", font=title_font, foreground=white, background=gray)
        addElement_title.place(relx=0.5, rely=0.1, anchor="center")

        # Back Button
        back_button = tk.Button(
            self, 
            text="Back", 
            font=standard_font, 
            background=darkergray, 
            foreground=white,
            activebackground = darkgray,
            activeforeground = white,
            command=lambda:controller.showFrame(FrontPage)
        )
        back_button.place(x=0, y=0, anchor="nw", width=100, height=50)

        label = tk.Label(
            self, 
            text = "Website", 
            font = title_font, 
            foreground = white, 
            background = gray
        )
        label.place(x=175, y=100)

        search_entry = tk.Entry(
            self, 
            font = standard_font
        )
        search_entry.place(x=360, y=175, anchor="e", width=200, height=25)


        label = tk.Label(
            self, 
            text = "Email", 
            font = title_font, 
            foreground = white, 
            background = gray
        )
        label.place(x=175, y=200)

        search_entry = tk.Entry(
            self, 
            font = standard_font
        )
        search_entry.place(x=360, y=275, anchor="e", width=200, height=25)


        label = tk.Label(
            self, 
            text = "Password", 
            font = title_font, 
            foreground = white, 
            background = gray
        )
        label.place(x=175, y=300)

        search_entry = tk.Entry(
            self, 
            font = standard_font
        )
        search_entry.place(x=360, y=375, anchor="e", width=200, height=25)

        add_button = tk.Button(
            self, 
            text = "ADD", 
            command = lambda : controller.showFrame(FrontPage)
        )
        add_button.place(x=600, y=600)


screen = TkinterApp()
screen.geometry("700x750")
screen.resizable(False, False)
screen.title("Password Manager")
icon = tk.PhotoImage(file='assets\icon.png')
screen.wm_iconphoto(False, icon)

screen.mainloop()
