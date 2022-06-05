#!/usr/bin/evn python3

import os
from cryptography.fernet import Fernet

files =[]

for file in os.listdir():
    if file == "snakes-encrypt.py" or file == "snakes-key.key" or file =="snakes-decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("snakes-key.key", "rb") as key:
    secretkey = key.read()



for file in files:
    with open(file, "rb") as thefile:
        contents =thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt (contents)

    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)