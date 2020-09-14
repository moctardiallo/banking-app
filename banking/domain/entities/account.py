from datetime import datetime as date

class Account:

    def __init__(self, solde):
        self.solde = solde

    def debit(self, amount, user):
        if self.solde < amount:
            raise ValueError("Impossible transaction because your solde is lower than the amount")
        else:
            old_solde = self.solde
            self.solde -= amount
        trans = Transaction(self.debit.__name__, user, amount, old_solde, self.solde)
        return trans

    def deposit(self, amount, user):
        old_solde = self.solde
        self.solde += amount
        trans = Transaction(self.deposit.__name__, user, amount, old_solde, self.solde)
        return trans

    def __eq__(self, other):
        return self.solde == other.solde

    def __str__(self):
        return str(self.solde)

class Transaction:
    def __init__(self, name, user, amount, old_solde, new_solde):
        self.name = name
        self.user = user
        self.amount = amount
        self.old_solde = old_solde
        self.new_solde = new_solde
        self.time = date.now().ctime()

    def __str__(self):
        return f'ACTION:{self.name}\nNAME: {self.user.name}\nOLD SOLDE: {self.old_solde}\n{self.name.upper()} AMOUNT: {self.amount}\nNEW_SOLDE: {self.new_solde}\nTRANSACTION TIME: {self.time}\n\n'

    def save(self, db):
        save_format = f'===={self.name.upper()} TANSACTION====\n{self}'
        return save_format

    def __eq__(self, other):
        return self.name == other.name and \
                self.user == other.user and \
                    self.old_solde == other.old_solde and \
                        self.new_solde == other.new_solde