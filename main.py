# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import os
import random

import Client
import PremiumClient
import Employee
import matrix
import passwordCheck

s = hashlib.sha3_256()
b = hashlib.sha3_256(b"Hello World!")
allUsers = []
passwords = [[]]


def print_hi(name):
    userPass = input("Please enter a password:")
    print(userPass)
    save = hashlib.sha3_256(userPass.encode())
    salt = hashlib.sha3_256(b"Hello")
    print(save.hexdigest() + salt.hexdigest())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readUsers():
    f = open("allUsers.txt", "r")
    userInfo = f.read()
    u = []
    for users in userInfo.split('\n'):
        u.append(users.split(';'))

    for singleUser in u:
        if singleUser[1] == "Client":
            allUsers.append(
                Client.Client(singleUser[2], singleUser[0], singleUser[3], singleUser[4], matrix.clientMatrix,
                              singleUser[1]))
        elif singleUser[1] == "Premium Client":
            allUsers.append(
                PremiumClient.PremiumClient(singleUser[2], singleUser[0], singleUser[3], singleUser[4],
                                            matrix.premiumClient,
                                            singleUser[1]))
        elif singleUser[1] == "Employee":
            allUsers.append(
                Employee.Employee(singleUser[0], singleUser[2], singleUser[1], singleUser[3], matrix.employee))
        elif singleUser[1] == "Financial Advisor":
            allUsers.append(
                Employee.Employee(singleUser[0], singleUser[2], singleUser[1], singleUser[3], matrix.financialAdvisor))
        elif singleUser[1] == "Financial Planner":
            allUsers.append(
                Employee.Employee(singleUser[0], singleUser[2], singleUser[1], singleUser[3], matrix.financialPlanner))
        elif singleUser[1] == "Investment Analyst":
            allUsers.append(
                Employee.Employee(singleUser[0], singleUser[2], singleUser[1], singleUser[3], matrix.investmentAnalyst))
    f.close()


def readPasswords():
    f = open("passwords.txt", "r")
    print(f.read())
    f.close()


# Press the green button in the gutter to run the script.

def addPassword(password, user):
    allSalts = []
    if passwordCheck.check(password, user):
        # print("Password accepted")
        file = open("passwords.txt", "a")
        salt = str(random.Random().randint(0, 1000000000))
        if os.stat("passwords.txt").st_size == 0:
            print("This ran once")
            file.write(str(user.getUserID()) + ";" + str(salt) + ";" + str(hashlib.sha3_256((password + salt).encode()).hexdigest()))
            return True
        for line in open("passwords.txt", "r"):
            if user.getUserID() == line.split(';')[0]:
                print("User already has a password")
                return False

        for temp in open("passwords.txt", "r"):
            allSalts = temp.split(';')[1]

        if salt in allSalts:
            salt = str(random.Random().randint(0, 1000000000))
       # print(str(user.getUserID()) + ";" + str(salt) + ";" + str(hashlib.sha3_256((password + salt).encode()).hexdigest()) + "\n")
        print(str(user.getUserID()))
        print(str(salt))
        #print(str(hashlib.sha3_256((password + salt).encode()).hexdigest()))

        file.write("\n")
        file.write(str(user.getUserID()) + ";" + str(salt) + ";" + str(hashlib.sha3_256((password + salt).encode()).hexdigest()))

        file.close()
    # print(user.getUserID())


if __name__ == '__main__':
    readUsers()
    userpassword1 = "Test1@12f"
    userpassword2 = "Test2@12f"
    userpassword3 = "Test3@12f"
    userpassword4 = "Test4@12f"
    #addPassword(userpassword1, allUsers[0])
    #addPassword(userpassword2, allUsers[1])
    #addPassword(userpassword3, allUsers[2])
    #addPassword(userpassword4, allUsers[3])
    print(passwordCheck.correctPassword(allUsers[0], userpassword1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
