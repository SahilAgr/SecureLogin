import matrix
class Employee:
    def __init__(self, userID, name, role, contactInfo, access):
        self.id = userID
        self.name = name
        self.contactInfo = contactInfo
        self.role = role
        if access == matrix.clientMatrix or access == matrix.premiumClient:
            print("Invalid access matrix")
        else:
            self.access = access

        """
        file = open('allUsers.txt', 'a')
        file.write(str(self.id) + ";")
        file.write(self.role + ";")
        file.write(self.name + ";")
        file.write(self.contactInfo + '\n')
        file.close()
        """

    def getName(self):
        return self.name

    def getContactInfo(self):
        return self.contactInfo

    def getAccess(self, file, permission):
        return self.access[file][permission]

    def getRole(self):
        return self.role

    def getUserID(self):
        return self.id

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
