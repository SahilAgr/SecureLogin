import unittest

import Client
import Employee
import PremiumClient
import main
import matrix
import passwordCheck


class MyTestCase(unittest.TestCase):
    def testUserCreation(self):
        client = Client.Client("Luffy", 1, 100, [], matrix.clientMatrix
                               , "Client")
        premClient = Client.Client("Zoro", 2, 100, [], matrix.premiumClient
                                   , "Premium Client")
        premiumClient = PremiumClient.PremiumClient(premClient)
        self.assertEqual(client.getName(), "Luffy")
        self.assertEqual(client.getUserID(), 1)
        self.assertEqual(client.getRole(), "Client")
        self.assertEqual(client.checkBalance(), 100)
        self.assertEqual(premiumClient.getName(), "Zoro")
        self.assertEqual(premiumClient.getUserID(), 2)
        self.assertEqual(premiumClient.getRole(), "Premium Client")
        self.assertEqual(premiumClient.checkBalance(), 100)
        self.assertEqual(premiumClient.getAccess(), matrix.premiumClient)
        self.assertEqual(client.getAccess(), matrix.clientMatrix)
        self.assertEqual(client.getPermissions(0, 0), 1)
        self.assertEqual(premiumClient.getPermissions(0, 0), 1)
        self.assertEqual(client.getPermissions(0, 1), 1)
        self.assertEqual(premiumClient.getPermissions(0, 1), 1)
        self.assertEqual(client.getPermissions(1, 0), 1)
        self.assertEqual(premiumClient.getPermissions(1, 0), 1)
        self.assertEqual(client.getPermissions(1, 1), 0)
        self.assertEqual(premiumClient.getPermissions(1, 1), 0)

    def testPasswords(self):
        client = Client.Client("Luffy", 1, 100, [], matrix.clientMatrix
                               , "Client")
        premClient = Client.Client("Zoro", 2, 100, [], matrix.premiumClient
                                   , "Premium Client")
        premiumClient = PremiumClient.PremiumClient(premClient)
        self.assertEquals(passwordCheck.check("password", client.getName()), False)
        self.assertEquals(passwordCheck.check("Test@12A", premiumClient.getName()), True)
        self.assertEquals(passwordCheck.check("12345Test", client.getName()), False)

    def checkResources(self):
        client = Client.Client("Luffy", 1, 100, [], matrix.clientMatrix
                               , "Client")
        emp = Employee.Employee(3, "Garp", "Teller", "garp@finvest.com", matrix.employeeMatrix)
        self.assertEquals(emp.readFile(4,0,"privateConsumerInstrument.txt", "You do not have permission to read this file"))
        self.assertEqual(emp.getAccess(), matrix.employeeMatrix)
        self.assertEqual(client.balance, 100)


if __name__ == '__main__':
    unittest.main()
