import sys

sys.path.insert(0, "./src")
import pkg_test_dprohe
import pytest


def test_add():
    assert pkg_test_dprohe.core.core_1.add(1, 2) == 1 + 2


def test_subtract():
    assert pkg_test_dprohe.core.core_1.subtract(2, 1) == 2 - 1
