"""
Binary Regular Expressions.
"""
from kyle.regex.regex import Regex


class Binary(Regex):
    """
    Abstract Binary Regular Expressions.
    """
    operator = None
    left = None
    right = None
    _parens = True

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_string(self):
        """
        Convert the component Regular Expressions and join them using
        self.operator.
        """
        unparenthesized = (
            self.left.to_string() + self.operator + self.right.to_string()
        )
        if self._parens:
            return '(' + unparenthesized + ')'
        return unparenthesized
