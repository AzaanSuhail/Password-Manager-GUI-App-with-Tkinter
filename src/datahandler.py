from . import metadata

import os

def save(website, email, password):
    with open(os.path.join(metadata.DATAPATH, "data.txt"), "a") as data_file:
        data = metadata.DATASEPERATOR.join([website.strip(), email.strip(), password.strip()])
        data_file.write(data + "\n")
        return True

def load():
    try:
        with open(os.path.join(metadata.DATAPATH, "data.txt"), "r") as data_file:
            lines = data_file.readlines()
            lines = [line.strip("\n") for line in lines]
            data = []
            for line in lines:
                item = line.split(metadata.DATASEPERATOR)
                data.append(item)
            return data
    except FileNotFoundError as _:
        return [[]]
