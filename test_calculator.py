from calculator_plus import Calculator

def test_add():
    result = Calculator.add(0,16,4)
    assert result == 20
def test_subtract():
    result = Calculator.subtract(0,16,4)
    assert result == 12
def test_multiply():
    result = Calculator.multiply(0,16,4)
    assert result == 64
def test_divide():
    result = Calculator.divide(0,16,4)
    assert result == 4
def test_divide_zero():
    result = Calculator.divide(0,16,0)
    assert result == 'Cannot divide by zero.'
def test_square_root():
    result = Calculator.square_root(0,25)
    assert result == 5 