from . import metadata

import pyperclip

import secrets
import string
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

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secure_password

def add_password_to_password_entry(password_entry, password):
    password_entry.delete(0, tk.END)
    password_entry.config(fg="black")
    password_entry.insert(0, password)

def copy_to_clipboard(password):
    pyperclip.copy(password)