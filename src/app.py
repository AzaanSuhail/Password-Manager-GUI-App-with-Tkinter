from . import commands
from . import eventhandler
from . import metadata
from .state import State

import os
import tkinter as tk
from ttkbootstrap import ttk

def create_write_tab(notebook):
    write_tab = ttk.Frame(master=notebook)

    title_label = ttk.Label(master=write_tab, text="Password Manager", font=metadata.HEADINGFONT)
    title_label.pack(padx=10, pady=10)

    frame = ttk.Frame(master=write_tab)
    frame.pack()
    frame.columnconfigure((0,5), weight=1, uniform="a")
    frame.rowconfigure((0,5), weight=1, uniform="a")

    website_label = ttk.Label(master=frame, text="Website:", font=metadata.FONT)
    website_label.grid(row=0, column=1, padx=12, pady=8)
    email_label = ttk.Label(master=frame, text="Email:", font=metadata.FONT)
    email_label.grid(row=1, column=1, padx=12, pady=8)
    password_label = ttk.Label(master=frame, text="Password:", font=metadata.FONT)
    password_label.grid(row=2, column=1, padx=12, pady=8)

    website_entry = ttk.Entry(master=frame, width=45, font=metadata.FONT)
    website_entry.grid(row=0, column=2, columnspan=2)
    email_entry = ttk.Entry(master=frame, width=45, font=metadata.FONT)
    email_entry.grid(row=1, column=2, columnspan=2)

    password_frame = ttk.Frame(master=frame, width=45)
    password_frame.columnconfigure((0,5), weight=1, uniform="c")
    password_frame.grid(row=2, column=2, columnspan=3)

    generate_password_button = ttk.Button(master=password_frame, text="Generate", command=lambda: eventhandler.handle_generate_event(password_entry))
    generate_password_button.grid(row=0, column=5, pady=5)

    password_entry = ttk.Entry(master=password_frame, width=39, font=metadata.FONT)
    password_entry.grid(row=0, column=0, columnspan=4)

    success_label = ttk.Label(master=frame, text="Saved Succcessfully!", font=metadata.FONT)
    success_label.grid(row=4, column=1, columnspan=3, pady=12)

    submit_button = ttk.Button(master=frame, text="Save", command=lambda: eventhandler.handle_submit_event(website_entry, email_entry, password_entry, success_label))
    submit_button.grid(row=3, column=1, columnspan=3,  pady=12)

    commands.create_placeholder(website_entry, metadata.WEBSITE_PLACEHOLDER)
    commands.create_placeholder(email_entry, metadata.EMAIL_PLACEHOLDER)
    commands.create_placeholder(password_entry, metadata.PASSWORD_PLACEHOLDER)

    notebook.add(write_tab, text="Write")

def create_read_tab(notebook):
    read_tab = ttk.Frame(master=notebook)

    title_label = ttk.Label(master=read_tab, text="Password Manager", font=metadata.HEADINGFONT)
    title_label.pack(padx=10, pady=10)

    frame = ttk.Frame(master=read_tab)
    frame.pack()
    frame.columnconfigure((0,5), weight=1, uniform="a")
    frame.rowconfigure((0,5), weight=1, uniform="a")

    website_label = ttk.Label(master=frame, text="Website:", font=metadata.FONT)
    website_label.grid(row=0, column=1, padx=12, pady=8)
    email_label = ttk.Label(master=frame, text="Email:", font=metadata.FONT)
    email_label.grid(row=1, column=1, padx=12, pady=8)

    website_entry = ttk.Entry(master=frame, width=45, font=metadata.FONT)
    website_entry.grid(row=0, column=2, columnspan=2)
    email_entry = ttk.Entry(master=frame, width=45, font=metadata.FONT)
    email_entry.grid(row=1, column=2, columnspan=2)

    output_label = ttk.Label(master=frame, text="output label!!", font=metadata.FONT)
    output_label.grid(row=4, column=1, columnspan=3, pady=12)

    submit_button = ttk.Button(master=frame, text="Get Password", command=lambda: eventhandler.handle_read_event(website_entry, email_entry, output_label))
    submit_button.grid(row=2, column=1, columnspan=3,  pady=12)

    commands.create_placeholder(website_entry, metadata.WEBSITE_PLACEHOLDER)
    commands.create_placeholder(email_entry, metadata.EMAIL_PLACEHOLDER)

    notebook.add(read_tab, text="Read")

def create_main_window():
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("800x500")
    window.minsize(400,400)
    window.iconbitmap(default=metadata.ICONPATH)
    
    notebook = ttk.Notebook(master=window)
    create_write_tab(notebook)
    create_read_tab(notebook)
    notebook.pack(fill="both")

    return window

def run(window):
    window.mainloop()

def main():
    app = create_main_window()
    run(app)
