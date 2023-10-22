from . import metadata

import os

def save(website, email, password):
    with open(os.path.join(metadata.DATAPATH, "data.txt"), "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        return True