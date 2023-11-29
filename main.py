# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import Client
import PremiumClient
import Employee
import matrix

s = hashlib.sha3_256()
b = hashlib.sha3_256(b"Hello World!")
passwords = [[]]


def print_hi(name):
    userPass = input("Please enter a password:")
    print(userPass)
    save = hashlib.sha3_256(userPass.encode())
    salt = hashlib.sha3_256(b"Hello")
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
    f.close()
    ##readPasswords()
    c1 = Client.Client("John", 1)
    print(c1.getName())
    print(c1.readFile(3, 0, "privateConsumerInstrument.txt"))
    # c3 = Client.Client("Sahil", 2)
    # c2 = PremiumClient.PremiumClient(c3)
    # print(c2.getInvestmentPortfolio)
    # c2.addInvestment("Apple")
    # print(c2.getInvestmentPortfolio)
    # c1.deposit(100)
    # c3.deposit(200)
    # c1.writeToFile()
    # c3.writeToFile()

    #print("hello" + str(2))

    e1 = Employee.Employee("Josh", "investmentAnalyst", "905-123-4567", matrix.investmentAnalyst)
    e1.readFile(3, 0, "privateConsumerInstrument.txt")
    e1.writeToFile(3, "hello", 1, "privateConsumerInstrument.txt")
    e1.readFile(3, 0, "privateConsumerInstrument.txt")
    print(e1.getName())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
