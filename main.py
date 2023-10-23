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
