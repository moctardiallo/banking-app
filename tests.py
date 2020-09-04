from banking.domain.pile import Pile
from banking.domain.client import Client
from banking.domain.account import Account, Transaction
from banking.domain.banque import Banque

import unittest

class TestPile(unittest.TestCase):
    def setUp(self):
        self.clients = Pile()

    def test_isEmpty(self):
        self.assertTrue(self.clients.is_empty())
        client = Client('Moctar', 'Diallo', 500)
        self.clients.push(client)
        self.assertFalse(self.clients.is_empty())

    def test_push(self):
        client = Client('Moctar', 'Diallo', 500)
        self.clients.push(client)
        self.assertNotEqual(self.clients.items, [])
        pushed = self.clients.items[-1]
        self.assertEqual(pushed.name, 'Moctar')
        self.assertEqual(pushed.lastname, 'Diallo')
        self.assertEqual(pushed.solde, 500)

    def test_pop(self):
        client = Client('Moctar', 'Diallo', 500)
        self.clients.push(client)
        popped = self.clients.pop()
        self.assertEqual(self.clients.items, [])
        self.assertEqual(popped.name, 'Moctar')
        self.assertEqual(popped.lastname, 'Diallo')
        self.assertEqual(popped.solde, 500)

    @unittest.skip('printer')
    def test_str(self):
        client1 = Client('Moctar', 'Diallo', 500)
        client2 = Client('Israel', 'Kuassi', 700)
        self.clients.push(client1)
        self.clients.push(client2)
        print()
        print(self.clients)

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client("Moctar", "Diallo", 500)

    def test_str(self):
        rep = "NAME: Moctar\nLASTNAME: Diallo\nSOLDE: 500\n\n"
        self.assertEqual(rep, str(self.client))

    def test_save(self):
        save_format = save_format = f"*********CLIENT ADDING*********\n{str(self.client)}"
        self.assertEqual(save_format, self.client.save())

    def test_create_client(self):
        client = Client.create_client('Moctar', 'Diallo', 500)
        self.assertIsInstance(client, Client)
        self.assertEqual(client.name, "Moctar")
        self.assertEqual(client.lastname, "Diallo")
        self.assertEqual(client.solde, 500)

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(500)

    def test_deposit(self):
        self.account.deposit(100, None)
        self.assertEqual(self.account.solde, 600)
    
    def test_debit(self):
        self.account.debit(100, None)
        self.assertEqual(self.account.solde, 400)

    def test_eq(self):
        self.assertEqual(self.account, Account(500))
        self.assertNotEqual(self.account, Account(600))
        self.assertNotEqual(self.account, Account(400))

    def test_str(self):
        self.assertEqual(str(self.account), '500')

class TestTransaction(unittest.TestCase):
    def test_str(self):
        pass

class TestBanque(unittest.TestCase):
    def setUp(self):
        self.banque = Banque()

    def test_createProfile(self):
        client = self.banque.create_profile('Moctar', 'Diallo', 500)
        self.assertIsInstance(client, Client)
        self.assertEqual(client.name, 'Moctar')
        self.assertEqual(client.lastname, 'Diallo')
        self.assertEqual(client.solde, 500)

    def test_makeTransaction(self):
        typ = 'deposit'
        client_name = 'Moctar'
        amount = 100
        self.banque.clients.push(Client('Moctar', 'Diallo', 500))
        trans = self.banque.make_transaction(typ, client_name, amount)
        client = self.banque.clients.pop()
        self.assertEqual(client.solde, 600)


if __name__ == '__main__':
    unittest.main()