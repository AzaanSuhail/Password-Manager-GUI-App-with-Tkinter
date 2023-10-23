from . import commands
from . import metadata
from . import eventhandler
from .state import State

import os
import tkinter as tk

def read_passwords():
    if State.is_reading_password == True:
        return
    
    State.is_reading_password = True
    read_window = tk.Toplevel()
    read_window.title("Read Passwords")
    read_window.config(padx=50, pady=50)

    # Labels
    website_label = tk.Label(master=read_window, text="Website:", font=metadata.FONT)
    website_label.grid(row=1, column=0)
    email_label = tk.Label(master=read_window, text="Email/Username:", font=metadata.FONT)
    email_label.grid(row=2, column=0)

    # Entries
    website_entry = tk.Entry(master=read_window, width=35, font=metadata.FONT)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()
    email_entry = tk.Entry(master=read_window, width=35, font=metadata.FONT)
    email_entry.grid(row=2, column=1, columnspan=2)

    password_label = tk.Label(master=read_window, text="Password", font=metadata.FONT)
    password_label.grid(row=4, column=0, columnspan=3)

    # ReadPasswordButton
    submit_button = tk.Button(master=read_window, text="Read Password", font=metadata.FONT, command=lambda: eventhandler.handle_read_event(website_entry, email_entry, password_label))
    submit_button.grid(row=3, column=0, columnspan=3)
    instance = True

def main():
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tk.Canvas(height=200, width=200)
    logo_img = tk.PhotoImage(file=os.path.join(metadata.RESOURCESPATH, "logo.png"))
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    # Labels
    website_label = tk.Label(text="Website:", font=metadata.FONT)
    website_label.grid(row=1, column=0)
    email_label = tk.Label(text="Email/Username:", font=metadata.FONT)
    email_label.grid(row=2, column=0)
    password_label = tk.Label(text="Password:", font=metadata.FONT)
    password_label.grid(row=3, column=0)

    # Entries
    website_entry = tk.Entry(width=35, font=metadata.FONT)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()
    email_entry = tk.Entry(width=35, font=metadata.FONT)
    email_entry.grid(row=2, column=1, columnspan=2)
    password_entry = tk.Entry(width=21, font=metadata.FONT)
    password_entry.grid(row=3, column=1)

    # Buttons
    generate_password_button = tk.Button(text="Generate Password", font=metadata.FONT, command=lambda: eventhandler.handle_generate_event(password_entry))
    generate_password_button.grid(row=3, column=2)
    submit_button = tk.Button(text="Submit", width=36, font=metadata.FONT, command=lambda: eventhandler.handle_submit_event(website_entry, email_entry, password_entry))
    submit_button.grid(row=4, column=1, columnspan=2)

    # ReadPasswordButton
    read_password_button = tk.Button(text="Read Passwords", font=metadata.FONT, command=read_passwords)
    read_password_button.grid(row=5, column=0, columnspan=3)

    # EventListener
    commands.create_placeholder(website_entry, metadata.WEBSITE_PLACEHOLDER)
    commands.create_placeholder(email_entry, metadata.EMAIL_PLACEHOLDER)
    commands.create_placeholder(password_entry, metadata.PASSWORD_PLACEHOLDER)

    window.mainloop()
