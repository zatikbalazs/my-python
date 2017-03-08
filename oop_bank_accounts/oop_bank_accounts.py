# My first object oriented programming (OOP) example.

class Account:
    def __init__(self, name, balance = 0, min_balance = 0):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount
        return "{} has been added to your balance.".format(amount)

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return "{} has been withdrawn from your balance.".format(amount)
        else:
            return "Transaction refused: not enough funds!"

    def show_statement(self):
        return "Name: {} >>>>> Current Balance: ${}".format(self.name, self.balance)

    def __str__(self):
        return "Bank account of: {}".format(self.name)

    def __del__(self):
        print("Account has been deleted.")
