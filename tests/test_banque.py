import unittest

from banking.domain.banque import Banque
from banking.domain.entities import Client

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