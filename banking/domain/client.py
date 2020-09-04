from .account import Account

class Client:
    def __init__(self, name, lastname, solde):
        self.name = name
        self.lastname = lastname
        self._account = Account(solde)

    # Equivalent of the 'createClient'
    @classmethod
    def create_client(cls, name, lastname, solde):
        return cls(name, lastname, solde)

    def __str__(self):
        return f"NAME: {self.name}\nLASTNAME: {self.lastname}\nSOLDE: {self._account}\n\n"

    # Equivalent to the 'clientCreatedFormatInFile' function
    def save(self):
        save_format = f"*********CLIENT ADDING*********\n{self}"
        return save_format
        
    def __eq__(self, other):
        return self.name == other.name and \
            self.lastname == other.lastname and \
                self._account == other._account

    @property
    def solde(self):
        return self._account.solde

    def deposit(self, amount):
        return self._account.deposit(amount, self)

    def debit(self, amount):
        return self._account.debit(amount, self)