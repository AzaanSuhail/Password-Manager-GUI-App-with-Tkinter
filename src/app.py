import metadata

import os
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tk.Canvas(height=200, width=200)
    logo_img = tk.PhotoImage(file=os.path.join(metadata.RESOURCESPATH, "logo.png"))
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    #Labels
    website_label = tk.Label(text="Website:")
    website_label.grid(row=1, column=0)
    email_label = tk.Label(text="Email/Username:")
    email_label.grid(row=2, column=0)
    password_label = tk.Label(text="Password:")
    password_label.grid(row=3, column=0)

    #Entries
    website_entry = tk.Entry(width=35)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()
    email_entry = tk.Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, "user@email.com")
    password_entry = tk.Entry(width=21)
    password_entry.grid(row=3, column=1)

    # Buttons
    generate_password_button = tk.Button(text="Generate Password", command=generate_password)
    generate_password_button.grid(row=3, column=2)
    add_button = tk.Button(text="Add", width=36, command=save)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()