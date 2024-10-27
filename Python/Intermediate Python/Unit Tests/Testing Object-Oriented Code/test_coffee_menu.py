import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
   def setUp(self):
      self.menu = CoffeeMenu()

   def test_get_price_existing_item(self):
      result = self.menu.get_price('americano')
      self.assertEqual(result, 2.70)

   def test_get_price_non_existing_item(self):
      self.assertIsNone(self.menu.get_price('spanish'))
   
   def test_add_item(self):
      self.menu.add_item('Macchiato', 3.50)
      self.assertIsNotNone(self.menu.get_price('Macchiato'))

if __name__ == "__main__":
   unittest.main()