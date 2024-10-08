import hashlib
import os
import random
import time
import time
import Client
import PremiumClient
import Employee
import matrix
import passwordCheck

allUsers = []
currentUser = None


def readUsers():
    f = open("allUsers.txt", "r")
    userInfo = f.read()
    u = []
    for users in userInfo.split('\n'):
        u.append(users.split(';'))
    if u[0][0] == '':
        return None

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
        elif singleUser[1] == "Teller":
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




# Press the green button in the gutter to run the script.

def addPassword(password, user):
    allSalts = []
    if passwordCheck.check(password, user.getName()):
        file = open("passwords.txt", "a")
        salt = str(random.Random().randint(0, 1000000000))
        if os.stat("passwords.txt").st_size == 0:
            file.write(str(user.getUserID()) + ";" + str(salt) + ";" + str(
                hashlib.sha3_256((password + salt).encode()).hexdigest()))
            return True
        for line in open("passwords.txt", "r"):
            if user.getUserID() == line.split(';')[0]:
                print("User already has a password")
                return False

        for temp in open("passwords.txt", "r"):
            allSalts = temp.split(';')[1]

        if salt in allSalts:
            salt = str(random.Random().randint(0, 1000000000))
        file.write("\n")
        file.write(str(user.getUserID()) + ";" + str(salt) + ";" + str(
            hashlib.sha3_256((password + salt).encode()).hexdigest()))

        file.close()


def welcomeAndLogin():
    print("Welcome to Finvest Holdings!")
    print("Would you like to login or create an account?")
    print("1. Login")
    print("2. Create an account")
    print("3. Exit")
    loginInut = input("Please select an option: ")
    if loginInut == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for user in allUsers:
            if user.getName().lower().strip() == username.lower().strip():
                if passwordCheck.correctPassword(user, password):
                    print("Welcome " + user.getName() + " your role is " + user.getRole())
                    currentUser = user
                    return currentUser
                else:
                    print("Incorrect password")
                    welcomeAndLogin()
                    break
    elif loginInut == "2":
        uId = random.Random().randint(0, 300)
        print("Would you like to create a Client account or an Employee Account?")
        print("1. Client")
        print("2. Employee")
        accountType = input("Please select an option: ")
        if accountType == "1":
            print("Would you like to create a regular account or a premium account?")
            print("1. Regular")
            print("2. Premium")
            clientType = input("Please select an option: ")
            if clientType == "1":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(Client.Client(name, uId, 0, [],
                                              matrix.clientMatrix, "Client"))
                addPassword(userPass, allUsers[-1])
                userFile = open(name + '.txt', 'x')
                userFile.write("Name: " + name + '\n')
                userFile.write("ID: " + str(uId) + '\n')
                userFile.write("Balance: " + str(0) + '\n')
                userFile.write("Investment Portfolio: " + str([]) + '\n')
                userFile.close()
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Client" + ";")
                file.write(name + ";")
                file.write(str(0) + ";")
                file.write(str([]))
                file.close()
                print("Account created!")
            if clientType == "2":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                temClient = Client.Client(name, uId, 0, [], matrix.premiumClient, "Premium Client")
                allUsers.append(PremiumClient.PremiumClient(temClient))
                addPassword(userPass, allUsers[-1])

                userFile = open(name + '.txt', 'x')
                userFile.write("Name: " + name + '\n')
                userFile.write("ID: " + str(uId) + '\n')
                userFile.write("Balance: " + str(0) + '\n')
                userFile.write("Investment Portfolio: " + str([]) + '\n')

                userFile.close()
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Client" + ";")
                file.write(name + ";")
                file.write(str(0) + ";")
                file.write(str([]))
                file.close()
                print("Account created!")
            else:
                print("Invalid input")
        if accountType == "2":
            print("What is your role?")
            print("1. Teller")
            print("2. Financial Advisor")
            print("3. Financial Planner")
            print("4. Investment Analyst")
            print("5. Technical Support")
            print("6. Compliance Officer")
            role = input("Please select an option: ")
            if role == "1":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(
                    Employee.Employee(uId, name, "Employee", name.strip() + "@finvest.com",
                                      matrix.employee))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Teller" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            if role == "2":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(
                    Employee.Employee(uId, name, "Financial Advisor", name.strip() + "@finvest.com",
                                      matrix.financialAdvisor))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Financial Advisor" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            if role == "3":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(
                    Employee.Employee(uId, name, "Financial Planner", name.strip() + "@finvest.com",
                                      matrix.financialPlanner))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Financial Planner" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            if role == "4":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(Employee.Employee(uId, name, "Investment Analyst",
                                                  name.strip() + "@finvest.com",
                                                  matrix.investmentAnalyst))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Investment Analyst" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            if role == "5":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(
                    Employee.Employee(uId, name, "Technical Support", name.strip() + "@finvest.com",
                                      matrix.technicalSupport))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Technical Support" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            if role == "6":
                name = input("Please enter your name: ")
                while True:
                    userPass = input("Please enter your password: ")
                    if passwordCheck.check(userPass, name):
                        break
                    else:
                        print("Password does not meet requirements")
                allUsers.append(Employee.Employee(uId, name, "Compliance Officer",
                                                  name.strip() + "@finvest.com",
                                                  matrix.complianceOfficer))
                addPassword(userPass, allUsers[-1])
                file = open('allUsers.txt', 'a')
                file.write('\n' + str(uId) + ";")
                file.write("Compliance Officer" + ";")
                file.write(name + ";")
                file.write(name.strip() + "@finvest.com")
                file.close()
                print("Account created!")
            else:
                print("Invalid input")
    if loginInut == "3":

        exit("Thank you for using Finvest Holdings!")
    else:
        print("Invalid input")
        welcomeAndLogin()


def updateAllUsers():
    # Clear the file first
    with open('allUsers.txt', 'w'):
        pass  # do nothing, just close it

    # Open the file in append mode
    with open('allUsers.txt', 'a') as userFile:
        first_user = True
        for user in allUsers:
            if not first_user:
                userFile.write('\n')  # Add newline if it's not the first user
            else:
                first_user = False

            if user.getRole() == "Client" or user.getRole() == "Premium Client":
                userFile.write(str(user.getUserID()) + ";")
                userFile.write(user.getRole() + ";")
                userFile.write(user.getName() + ";")
                userFile.write(str(user.checkBalance()) + ";")
                userFile.write(str(user.investmentPortfolio))
            else:
                userFile.write(str(user.getUserID()) + ";")
                userFile.write(user.getRole() + ";")
                userFile.write(user.getName() + ";")
                userFile.write(user.getContactInfo())

    print("Users updated successfully!")




if __name__ == '__main__':
    readUsers()
    currentUser = welcomeAndLogin()
    if time.localtime().tm_hour > 17 and currentUser.getRole() == "Teller":
        print("Good evening " + currentUser.getName() + " your role is " + currentUser.getRole())
        print("You do not have access to the system after 5PM")

    while True:
        if currentUser is None:
            print("User not found, please try again")
        else:
            if currentUser.access[0][0] == 1:
                print("1. User Information")
            if currentUser.access[0][1] == 1:
                print("2. Modify User Information")
            if currentUser.access[1][0] == 1:
                print("3. View Bank Balance")
                print("4. Deposit")
                print("5. Withdraw")
            if currentUser.access[2][0] == 1:
                print("6. View Investment Portfolio")
            if currentUser.access[3][0] == 1:
                print("7. View Private Consumer Instrument")
            if currentUser.access[4][0] == 1:
                print("8. View Money Market Instruments")
            if currentUser.access[5][0] == 1:
                print("9. View Derivatives Trading")
            if currentUser.access[6][0] == 1:
                print("10. View Interest Instruments")
            if currentUser != None:
                print("11. Logout")

            userInput = input("Please select an option: ")
            if userInput == "1":
                if currentUser.getRole() == "Client" or currentUser.getRole() == "Premium Client":
                    currentUser.readFile(0, 0, currentUser.getName() + ".txt")
                else:
                    getUser = input("Please enter the name of the user you would like to view: ")
                    for user in allUsers:
                        if user.getName() == getUser:
                            user.readFile(0, 0, getUser + ".txt")
            elif userInput == "2":
                newName = input("Please enter your new name: ")
                currentUser.setName(newName)
            elif userInput == "3":
                if currentUser.getRole() == "Client" or currentUser.getRole() == "Premium Client":
                    print(currentUser.checkBalance())
                else:
                    getUser = input("Please enter the name of the user you would like to view: ")
                    for user in allUsers:
                        if user.getName() == getUser:
                            print(user.checkBalance())
            elif userInput == "4":
                amount = input("How much would you like to deposit: ")
                print("Your balance now reads: " + str(currentUser.deposit(amount)))
            elif userInput == "5":
                amount = input("How much would you like to withdraw: ")
                print("Your balance now reads: " + str(currentUser.withdraw(amount)))
            elif userInput == "6":
                print(currentUser.investmentPortfolio)
            elif userInput == "7":
                currentUser.readFile(3, 0, "privateConsumerInstrument.txt")
            elif userInput == "8":
                currentUser.readFile(4, 0, "moneyMarketInstruments.txt")
            elif userInput == "9":
                currentUser.readFile(5, 0, "derivativesTrading.txt")
            elif userInput == "10":
                currentUser.readFile(6, 0, "interestInstruments.txt")
            elif userInput == "11":
                currentUser = None
                updateAllUsers()
                currentUser = welcomeAndLogin()
            else:
                print("Invalid input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
