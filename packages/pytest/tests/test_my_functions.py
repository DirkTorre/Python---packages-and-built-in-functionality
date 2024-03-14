import pytest
import time

import source.my_functions as my_functions

def test_add():
    """
    Test the add function.
    """

    result = my_functions.add(1, 4)

    assert result == 5


def test_add_strings():
    """
    Test if both values are numbers.
    """

    result = my_functions.add("a ", "test")

    assert result == "a test"


def test_divide():
    """
    Test the divide function.
    """

    result = my_functions.divide(10, 5)

    assert result == 2


def test_divide_by_zero():
    """
    Test if the function gives a error if it divides by 0.
    This is good, because dividing by zero causes the universe to explode.
    """

    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    """
    Test to showcase how you ase marks (tags).
    """
    time.sleep(5)

    result = my_functions.divide(10, 5)

    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3


@pytest.mark.xfail(reason="We know we can not divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)