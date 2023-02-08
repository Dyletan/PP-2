# 5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Not enough money!")

acc1 = Account("Jack", 100)
print(acc1.balance)
acc1.deposit(30)
print(acc1.balance)
acc1.withdraw(70)
print(acc1.balance)
acc1.withdraw(100)
