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
allEmployees = []
allClients = []
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

    # print("hello" + str(2))

    allClients.append(Client.Client("Mischa Lowery", 123))
    allClients.append(Client.Client("Veronica Perez", 124))
    allClients.append(PremiumClient.PremiumClient(Client.Client("Willow Gara", 100)))
    allClients.append(PremiumClient.PremiumClient(Client.Client("Nala Preston", 101)))
    allEmployees.append(Employee.Employee("Winston Callahan", "Teller", "winston@email.com", matrix.employee))
    allEmployees.append(Employee.Employee("Kelan Gough", "Teller", "kelan@email.com", matrix.employee))
    allEmployees.append(Employee.Employee("Nelson Wilkins", "Financial Advisor", "nelson@email.com", matrix.financialAdvisor))
    allEmployees.append(
        Employee.Employee("Kelsie Chang", "Financial Advisor", "kelsie@email.com", matrix.financialAdvisor))
    allEmployees.append(
        Employee.Employee("Howard Linkler", "Compliance Officer", "howard@email.com", matrix.complianceOfficer))
    allEmployees.append(
        Employee.Employee("Stefania Smart", "Compliance Officer", "stefania@email.com", matrix.complianceOfficer))
    allEmployees.append(
        Employee.Employee("Stacy Kent", "Investment Analyst", "stacy@email.com", matrix.investmentAnalyst))
    allEmployees.append(
        Employee.Employee("Keikilana Kapahu", "Investment Analyst", "keikilana@email.com", matrix.investmentAnalyst))
    allEmployees.append(
        Employee.Employee("Kodi Matthews", "Financial Planner", "kodi@email.com", matrix.financialPlanner))
    allEmployees.append(
        Employee.Employee("Maliikah Wu", "Financial Planner", "malikah@email.com", matrix.financialPlanner))
    allEmployees.append(
        Employee.Employee("Caroline Lopez", "Technical Support", "caroline@email.com", matrix.technicalSupport))
    allEmployees.append(
        Employee.Employee("Pawel Barclay", "Technical Support", "pawel@email.com", matrix.technicalSupport))

    print(allEmployees[6].getAccess(4, 1))






    """allEmployees[0].readFile(3, 0, "privateConsumerInstrument.txt")
    allEmployees[0].writeToFile(3, "hello", 1, "privateConsumerInstrument.txt")
    allEmployees[0].readFile(3, 0, "privateConsumerInstrument.txt")
    print(allEmployees[0].getName())"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
