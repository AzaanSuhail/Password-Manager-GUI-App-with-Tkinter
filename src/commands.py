from . import metadata

import pyperclip

from random import choice
from random import randint
from random import shuffle
import tkinter as tk
from tkinter import messagebox

def is_valid(website, email, password):
    condition1 = (website == metadata.WEBSITE_PLACEHOLDER) or (len(website) == 0)
    condition2 = (email == metadata.EMAIL_PLACEHOLDER) or   (len(email) == 0)
    condition3 = (password == metadata.PASSWORD_PLACEHOLDER) or (len(password) == 0)
    
    if condition1 or condition2 or condition3:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return False
    return True

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)

def create_placeholder(entry, placeholder):
    def selecttext_on_focus():
        def select_text(event):
            if entry.get() == placeholder:
                entry.select_range(0, 'end')
        
        entry.bind("<FocusIn>", select_text)

    def placeholder_color():
        def changecolor(event):
            if entry.get() == placeholder:
                entry.config(fg="gray")
            else:
                entry.config(fg="black")
                
        entry.bind("<KeyRelease>", changecolor)
    
    selecttext_on_focus()
    placeholder_color()
    entry.insert(0, placeholder)
    entry.config(fg="gray")

def restore_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="gray")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    return "".join(password_list)

def add_password_to_password_entry(password_entry, password):
    password_entry.delete(0, tk.END)
    password_entry.config(fg="black")
    password_entry.insert(0, password)

def copy_to_clipboard(password):
    pyperclip.copy(password)