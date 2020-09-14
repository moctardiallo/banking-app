import unittest

from banking.domain.entities.client import Client


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

if __name__ == '__main__':
    unittest.main()