from division import *

def test_division():
    assert division(4, 2) == 2
    assert division(10, 2) == 5
    assert division(0.009, 0.003) == 3, "error"
    assert division(4, 0) == "Division by Zero"
    
def test_values():
    assert division("a", 2) == "Type Error"
    assert division([4], 2) == "Type Error"
    assert division(4.4, 2) == 2.2
    assert division(None, 2) == "Type Error"

if __name__== '__main__':
    test_division()
    test_values()
    print("OK")
    
