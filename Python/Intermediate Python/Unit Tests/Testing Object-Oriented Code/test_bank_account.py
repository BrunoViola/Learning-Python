import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
   def setUp(self):
      self.account = BankAccount(100)

   def tearDown(self):
      self.account = None

   def test_initial_balance(self):
      self.assertEqual(self.account.balance, 100)

if __name__ == "__main__":
   unittest.main()