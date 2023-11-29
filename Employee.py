class Employee:
    def __init__(self, name, role, contactInfo, access):
        self.name = name
        self.contactInfo = contactInfo
        self.role = role
        self.access = access

    def getName(self):
        return self.name

    def getContactInfo(self):
        return self.contactInfo

    def getAccess(self, file, permission):
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

