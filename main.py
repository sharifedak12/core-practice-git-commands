import pytest


def always_returns_true():
    return "Ada"


def test_always_returns_true():
    assert always_returns_true()

def always_return_false():

    return False
