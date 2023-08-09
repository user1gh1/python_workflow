import unittest
import os
import yaml
from division import *


with open('config.yaml', 'r') as file:
    config: dict = yaml.safe_load(file)
print(config['number1'])
#x = yaml.load("""a: 45\nb: cheese\nc: 7.8""")

number1 = os.environ.get('number1')
number2 = os.environ.get('number2')
answer = os.environ.get('answer')

print (number1)
number1 = os.getenv("number1")
print (number1)



class DivisionTest(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(4, 2) , 2)
        self.assertEqual(division(10, 2) , 5)
        self.assertEqual(division(0.009, 0.003) , 3)
        self.assertEqual(division(number1,number2) , answer)
        
        
if  __name__ == '__main__':
    unittest.main()