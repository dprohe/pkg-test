"""
docstring for src.pkg_test_dprohe.extras.extras_2
"""

from ..core.core_2 import multiply, divide


class Multiplier:
    """
    Docstring for Multiplier
    """

    def __init__(self, value: int | float | complex):
        """Create a multiplier class that multiplies specific value to numbers

        Parameters
        ----------
        value : int | float | complex
            A value that will be multiplied by any input
        """
        self.value = value

    def multiply(self, value: int | float | complex):
        """Multiplies a value

        Parameters
        ----------
        value : int | float | complex
            A value to add to

        Returns
        -------
        product : int | float | complex
            The multiplication of the two values
        """
        return multiply(self.value, value)


class Dividor:
    """
    Docstring for Dividor
    """

    def __init__(self, value: int | float | complex):
        """Create an dividor class that divides specific value from numbers

        Parameters
        ----------
        value : int | float | complex
            A value that will be divided from any input
        """
        self.value = value

    def divide(self, value: int | float | complex):
        """Divides a value

        Parameters
        ----------
        value : int | float | complex
            A value to divide from

        Returns
        -------
        ratio : int | float | complex
            The division of the two values
        """
        return divide(value, self.value)
