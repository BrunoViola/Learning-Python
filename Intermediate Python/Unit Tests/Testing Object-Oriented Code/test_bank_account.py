import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
   def setUp(self):
      self.account = BankAccount(100)

   def tearDown(self):
      self.account = None

   def test_initial_balance(self):
      self.assertEqual(self.account.balance, 100)

   def test_deposit(self):
      self.account.deposit(150)
      self.assertEqual(self.account.balance, 250)
   
   def test_negative_deposit(self):
      with self.assertRaises(ValueError):
       self.account.deposit(-50)
      
   def test_zero_deposit(self):
      with self.assertRaises(ValueError):
         self.account.deposit(0)
      
   def test_withdraw(self):
      self.account.withdraw(10)
      self.assertEqual(self.account.balance, 90)

   def test_negative_withdraw(self):
      with self.assertRaises(ValueError):
         self.account.withdraw(-30)
   
   def test_zero_withdraw(self):
      with self.assertRaises(ValueError):
         self.account.withdraw(0)

   def test_insufficient_funds_withdraw(self):
      with self.assertRaises(ValueError):
         self.account.withdraw(110)

if __name__ == "__main__":
   unittest.main()