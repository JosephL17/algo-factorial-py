# import pytest
from factorial import factorial

def test_factorial():
    assert factorial(4) == 24

def test_factorial_2():
    assert factorial(9) == 362880