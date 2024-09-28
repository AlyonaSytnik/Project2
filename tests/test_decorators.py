import pytest

from src.decorators import log, my_function


def test_my_function():
    assert my_function(1, 2)


def test_exception_decorator():
    with pytest.raises(
        Exception,
        match="my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '1'), {}",
    ):
        my_function(1, "1")


def test_right_decorator(capsys):
    x1, y1 = capsys.readouterr()
    r = x1 + y1
    with pytest.raises(Exception, match=f"my_function {r}"):
        my_function(x1, y1)
