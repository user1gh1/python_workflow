import unittest
import os
import yaml
from division import *
from pprint import pprint


with open('./.github/workflows/check.yaml', 'r') as file:
    config: dict = yaml.safe_load(file)
pprint(config, sort_dicts=False)
#print(config['number1'])
#x = yaml.load("""a: 45\nb: cheese\nc: 7.8""")
a = dict[True]['workflow_dispatch']['inputs']['number1']['default']
b = dict[True]['workflow_dispatch']['inputs']['number2']['default']
c = dict[True]['workflow_dispatch']['inputs']['answer']['default']
print (a)
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