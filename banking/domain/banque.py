from .pile import Pile
from .client import Client


class Banque:
    """
    Une banque ici est modelisee par une pile de clients
    A little awkward..
    """
    def __init__(self):
        self.clients = Pile()
        self.transactions = Pile()

    def enter(self):
        return "\n================Welcome To ISI Bank================\n"


    def request(self):
        return "1- Create your Banking Profil / For this choose 1\n" +\
               "2- Credit your account / For this choose 2\n" +\
               "3- Debit your account / For this choose 3\n" +\
               "4- Display the Stack Content / For this choose 4\n" +\
               "0- Quit the Bank / For this choose 4\n" +\
               "==================================================="

    @property
    def options(self):
        return [1, 2, 3, 4, 0]

            
    def create_profile(self, name, last_name, solde):
        client = Client.create_client(name, last_name, solde)
        self.clients.push(client)
        return client

    def make_transaction(self, typ, client_name, amount):
        popped = Pile()
        client = self.clients.pop()
        trans = None
        while client.name != client_name:
            popped.push(client)
            client = self.clients.pop()
        # we found a matching client
        if typ == 'deposit':
            trans = client.deposit(amount)
        elif typ == 'debit':
            trans = client.debit(amount)
        self.clients.push(client)
        while not popped.is_empty():
            self.clients.push(popped.pop())
        return trans
        

    # Equivalent to 'displayClients' function
    def __str__(self):
        return f"{str(self.clients)}"