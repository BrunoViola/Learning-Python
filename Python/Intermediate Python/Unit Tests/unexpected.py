import unittest, math

def get_sqrt(n):
   return math.sqrt(n)

def divide(a, b):
   return a/b

class TestUnexepected(unittest.TestCase):
   def test_valid_sqrt(self):
      with self.assertRaises(ValueError):
         get_sqrt(-16)

   def test_sqrt(self):
      result = get_sqrt(16)
      self.assertEqual(result, 4)
   
   def test_divide_by_(self):
      with self.assertRaises(ZeroDivisionError):
         divide(16/0)
   
   def test_divide(self):
      result = divide(16, 4)
      self.assertEqual(result, 4)
   

if __name__ == "__main__":
   unittest.main()