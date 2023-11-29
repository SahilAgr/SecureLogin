import Client
import matrix


class PremiumClient(Client.Client):
    def __init__(self, client):
        self.name = client.name
        self.id = client.id
        self.balance = client.balance
        self.investmentPortfolio = client.investmentPortfolio
        self.access = matrix.premiumClient

    def addInvestment(self, investment):
        self.investmentPortfolio.append(investment)

    def removeInvestment(self, investment):
        self.investmentPortfolio.remove(investment)

