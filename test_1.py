import pytest
from Calculator import Calculator


def test_add():
    assert Calculator.add(2, 2) == 4
    assert Calculator.add(-2, 5) == 3
    assert Calculator.add(0, 5) == 5
    assert Calculator.add(5.5, 5) == 10.5
    with pytest.raises(TypeError):
        Calculator.add("a", 5)
        Calculator.add(None, 5)
        Calculator.add({}, 5)
        Calculator.add([1, 2], 5)


def test_subtract():
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(-2, 5) == -7
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(5.5, 5) == 0.5
    with pytest.raises(TypeError):
        Calculator.subtract("a", 5)
        Calculator.subtract(None, 5)
        Calculator.subtract({}, 5)
        Calculator.subtract([1, 2], 5)


def test_multiply():
    assert Calculator.multiply(2, 2) == 4
    assert Calculator.multiply(-2, 5) == -10
    assert Calculator.multiply(0, 5) == 0
    assert Calculator.multiply(5.5, 5) == 27.5
    assert Calculator.multiply("a", 5) == "aaaaa"
    assert Calculator.multiply([1, 2], 5) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    with pytest.raises(TypeError):
        Calculator.multiply(None, 5)
        Calculator.multiply({}, 5)


def test_divide():
    assert Calculator.divide(2, 2) == 1
    assert Calculator.divide(-10, 5) == -2
    assert Calculator.divide(0, 5) == 0
    assert Calculator.divide(10, 0.5) == 20
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)
    with pytest.raises(TypeError):
        Calculator.divide("a", 5)
        Calculator.divide([1, 2], 5)
        Calculator.divide(None, 5)
        Calculator.divide({}, 5)