import pytest


def always_returns_true():
<<<<<<< HEAD

    return "ABC123"
=======
    return "Hello, world!"
>>>>>>> c074f653b40f8ba9b98248d5cd2424df89240456


def test_always_returns_true():
    assert always_returns_true()

def always_return_false():

    return False
