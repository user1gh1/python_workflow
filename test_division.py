import unittest

from division import *

class DivisionTest(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(4, 2), 2)
        self.assertEqual(division(10, 2) , 5)
        self.assertEqual(division(0.009, 0.003) , 3)
        
        
if  __name__ == '__main__':
    unittest.main()