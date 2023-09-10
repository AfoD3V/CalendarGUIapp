import pytest
from my_code import utils


def test_add_1():
    assert utils.test_function(1) == 2


def test_add_2():
    assert utils.test_function(2) != 0
