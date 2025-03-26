import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
   def test_reverse(self):
      result = string_utils.reverse_string('bit')
      self.assertEqual(result, 'tib')

   def test_capitalize(self):
      result = string_utils.capitalize_string('byte')
      self.assertEqual(result, 'Byte')
   
   def test_is_capitalized(self):
      result = string_utils.is_capitalized('Giga')
      self.assertTrue(result)

if __name__ == "__main__":
   unittest.main()