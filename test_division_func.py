from utils import division
import pytest

@pytest.mark.parametrize("a, b, result", [(18, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, result):
    assert division(a, b) == result

"""Проверка деления на 0, некорректного ввода"""
@pytest.mark.parametrize("expection, divider, divis", [(ZeroDivisionError, 0, 18),
                                                          (TypeError, "2", 20)])
def test_division_error(expection, divider, divis):
    with pytest.raises(expection):
        division(divis, divider)

