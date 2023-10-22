from . import commands
from . import datahandler

def handle_add_event(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if commands.is_valid(website, email, password):
        success = datahandler.save(website, email, password)
        if success:
            print("successfuly inserted to data.txt")
    
    commands.clear_entries(website_entry, email_entry, password_entry)

def handle_generate_event(password_entry):
    password = commands.generate_password()
    commands.add_password_to_password_entry(password_entry, password)
    commands.copy_to_clipboard(password)