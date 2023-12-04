import os
import matrix


class Client:
    def __init__(self, name, userID, balance, investmentPortfolio, access, role):
        self.name = name
        self.id = userID
        self.balance = balance
        self.investmentPortfolio = investmentPortfolio
        if access == matrix.clientMatrix or access == matrix.premiumClient:
            self.access = access
        else:
            print("Invalid access matrix")
        self.role = role

        # os.mkdir(self.name)
        # os.chdir(self.name)
        """
        file = open('allUsers.txt', 'a')
        file.write(str(self.id) + ";")
        file.write(self.role + ";")
        file.write(self.name + ";")
        file.write(str(self.balance) + ";")
        file.write(str(self.investmentPortfolio) + '\n')

        file.close()
        """
        # os.chdir('C:/Users/sahil/Desktop/school ish/y5/last sem/4810/assign')

    def deposit(self, amount):
        first = int(self.balance)
        second = int(amount)
        self.balance = first + second
        return self.balance

    def withdraw(self, amount):
        first = int(self.balance)
        second = int(amount)
        if first < second:
            return 'Insufficient funds'
        else:
            self.balance = first - second
            return self.balance

    def checkBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getUserID(self):
        return self.id

    def getRole(self):
        return self.role

    @property
    def getInvestmentPortfolio(self):
        return self.investmentPortfolio

    def writeToFile(self):
        os.chdir(self.name)
        file = open('userInfo.txt', 'w')
        file.write("Name: " + self.name + '\n')
        file.write(str("UserID" + str(self.id) + '\n'))
        file.write(str("Bank Balance: " + self.balance) + '\n')
        file.write(str(self.investmentPortfolio) + '\n')
        file.close()
        os.chdir('C:/Users/sahil/Desktop/school ish/y5/last sem/4810/assign')
        return 0

    def getPermissions(self, file, permission):
        return self.access[file][permission]

    def readFile(self, file, permission, fileName):
        if self.access[file][permission] == 1:
            f = open(fileName, "r")
            print(f.read())
            f.close()
        else:
            print("You do not have permission to read this file")

    def writeToFile(self, file, text, permission, fileName):
        if self.access[file][permission] == 1:
            f = open(fileName, "a")
            f.write(text)
            f.close()
        else:
            print("You do not have permission to write to this file")
