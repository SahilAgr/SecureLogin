# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import sys

from tabulate import tabulate

import test

s = hashlib.sha3_256()
b = hashlib.sha3_256(b"Hello World!")
passwords = [[]]


def print_hi(name):
    userPass = input("Please enter a password:")
    print(userPass)
    save = hashlib.sha3_256(userPass.encode())
    salt = hashlib.sha3_256(b"Hello");
    print(save.hexdigest() + salt.hexdigest())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readPasswords():
    f = open("passwords.txt", "r")
    print(f.read())
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("passwords.txt", "a")
    s.update(b"Hello World!")
    passwords.append(("1", "1234", s.hexdigest()))
    passwords.append(("2", "2345", b.hexdigest()))
    passwords.append(("3", "5678", s.hexdigest()))
    titles = ["ID", "Salt", "Hash"]
    #print(tabulate(passwords, headers=titles))
    f.write(tabulate(passwords, headers=titles))
    f.close()
    readPasswords()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
