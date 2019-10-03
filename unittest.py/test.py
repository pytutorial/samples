import unittest

def add(a, b):
   return a + b

class TestCase1(unittest.TestCase):

   def test1(self):
       self.assertEqual(add(1, 2), 3)

   def test2(self):
       self.assertTrue(add(1, 2) == 3)
       self.assertFalse(add(1, 2) > 3)

if __name__ == '__main__':
   unittest.main()