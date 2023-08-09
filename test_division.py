import unittest
import os

number1 = os.environ.get('number1')
number2 = os.environ.get('number2')
answer = os.environ.get('answer')

from division import *

class DivisionTest(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(4, 2) , 2)
        self.assertEqual(division(10, 2) , 5)
        self.assertEqual(division(0.009, 0.003) , 3)
        self.assertEqual(division(number1,number2) , answer)
        
        
if  __name__ == '__main__':
    unittest.main()