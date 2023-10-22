from . import metadata

import pyperclip

import os
from random import choice
from random import randint
from random import shuffle
import tkinter as tk
from tkinter import messagebox

def is_valid(website, email, password):
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return False
    return True

def save(website, email, password):
    with open(os.path.join(metadata.DATAPATH, "data.txt"), "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        return True

def clear_entries(website_entry, email_entry, password_entry):
    website_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

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
    password_entry.insert(0, password)

def copy_to_clipboard(password):
    pyperclip.copy(password)

def handle_add_event(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if is_valid(website, email, password):
        success = save(website, email, password)
        if success:
            print("successfuly inserted to data.txt")
    
    clear_entries(website_entry, email_entry, password_entry)

def handle_generate_event(password_entry):
    password = generate_password()
    add_password_to_password_entry(password_entry, password)
    copy_to_clipboard(password)