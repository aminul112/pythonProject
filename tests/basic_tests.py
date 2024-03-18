from calculator import Calculator
from main import addition


def test_addition():

    obj1 = Calculator(x=100, y=50)
    assert  obj1.addition() == 150

def test_subtraction():

    obj1 = Calculator(x=100, y=50)
    assert  obj1.subtract() == 50