import unittest

from banking.domain.entities.account import Account


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

if __name__ == '__main__':
    unittest.main()