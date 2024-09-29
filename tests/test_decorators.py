import pytest

from src.decorators import log, my_function


def test_my_function():
    assert my_function(1, 2)


def test_exception_decorator():
    with pytest.raises(TypeError):
        my_function(1, "2")


def test_right_decorator(capsys):
    ret = my_function(1, 2)
    out, err = capsys.readouterr()
    assert out == "my_function 3\n\n"
    assert ret == 3
