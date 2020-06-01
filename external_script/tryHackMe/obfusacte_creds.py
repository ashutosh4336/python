#!/usr/bin/env python3

"""
This script is used to create the file contents of `.creds`
which will be hidden file inside of the anonymous FTP folder
"""


from Crypto.Util.number import bytes_to_long
import pickle
import random


ssh_username = 'pwndev'
ssh_password = 'p1ckl2_@all_@r0und_th3_w0rld'

data = []

for index, charcter in enumerate(ssh_username):
    # print(index, charcter)
    data.append((f"ssh_user{index}", charcter))


for index, charcter in enumerate(ssh_password):
    # print(index, charcter)
    data.append((f"ssh_pass{index}", charcter))


random.shuffle(data)
pickled = pickle.dumps(data)
print(len(bin(bytes_to_long(pickled))[2:]))
