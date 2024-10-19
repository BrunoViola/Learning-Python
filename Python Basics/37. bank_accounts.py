class BankAccount:
   def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
      self.first_name = first_name
      self.last_name = last_name
      self.account_id = account_id
      self.account_type = account_type
      self.pin = pin
      self.balance = balance

   def deposit(self, amount_deposit):
      self.balance += amount_deposit
      return self.balance
   
   def withdraw(self, amount_withdraw):
      if (self.balance-amount_withdraw)>0:
         self.balance-=amount_withdraw
      else:
         print('The withdraw amount is higher than the balance')
      return self.balance
   
   def display_balance(self):
      print(f'{self.first_name}\'s balance is {self.balance} dollars')

ana = BankAccount('Ana', 'Peixoto', 1, 'Checking Account', 1, 997.12)
ana.display_balance()
ana.deposit(3.00)
ana.display_balance()
ana.withdraw(1000.13)
ana.withdraw(500.12)
ana.display_balance()