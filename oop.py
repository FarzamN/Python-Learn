class Account:
    def __init__(self, balance, accountNumber):
        self.balance = balance
        self.accountNumber = accountNumber

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount}, was debeted")
        print(f"Total balance: {self.getBalance()}")

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount}, was creadit")
        print(f"Total balance: {self.getBalance()}")

    def getBalance(self):
        return self.balance


acc1 = Account(1000, 1234)
acc1.debit(100)
acc1.credit(500)
#
# print(acc1.balance)
# print(acc1.accountNumber)
