# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import sys
import test

s = hashlib.sha3_256()
b = hashlib.sha3_256(b"Hello World!")


def print_hi(name):
    userPass = input("Please enter a password:")
    print(userPass)
    save = hashlib.sha3_256(userPass.encode())
    print(save.hexdigest())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s.update(b"Hello World!")

    print(s.hexdigest())
    print(b.hexdigest())
    print(s.hexdigest() == b.hexdigest())
    print_hi('PyCharm')
    test.printWords("Hello World!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


