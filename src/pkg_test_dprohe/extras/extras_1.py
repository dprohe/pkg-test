"""
Docstring for src.pkg_test_dprohe.extras.extras_1
"""

from ..core.core_1 import add, subtract


class Adder:
    """
    Docstring for Adder
    """

    def __init__(self, value: int | float | complex):
        """Create an adder class that a specific value to numbers

        Parameters
        ----------
        value : int | float | complex
            A value that will be added to any input
        """
        self.value = value

    def add(self, value: int | float | complex):
        """Adds a value

        Parameters
        ----------
        value : int | float | complex
            A value to add to

        Returns
        -------
        sum : int | float | complex
            The addition of the two values
        """
        return add(self.value, value)


class Subtractor:
    """
    Docstring for Subtractor
    """

    def __init__(self, value: int | float | complex):
        """Create an subtractor class that subtracts specific value from numbers

        Parameters
        ----------
        value : int | float | complex
            A value that will be subtracted from any input
        """
        self.value = value

    def subtract(self, value: int | float | complex):
        """Subtracts a value

        Parameters
        ----------
        value : int | float | complex
            A value to subtract from

        Returns
        -------
        difference : int | float | complex
            The subtraction of the two values
        """
        return subtract(value, self.value)
