import unittest

from banking.domain.entities.pile import Pile
from banking.domain.entities import Client


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

if __name__ == '__main__':
    unittest.main()