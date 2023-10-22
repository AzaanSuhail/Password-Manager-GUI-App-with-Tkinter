# import metadata

# import os
# from tkinter import messagebox
# from random import choice, randint, shuffle


# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# #Password Generator Project
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)

#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():

#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
#                                                       f"\nPassword: {password} \nIs it ok to save?")
#         if is_ok:
#             with open(os.path.join(metadata.DATAPATH, "data.txt"), "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)

from src import app
from src import metadata

import os

def init():
    if not os.path.exists(metadata.DATAPATH):
        os.makedirs(metadata.DATAPATH)

def main():
    app.main()

if __name__ == "__main__":
    init()
    main()