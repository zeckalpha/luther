"""
Unary Regular Expressions.
"""
from kyle.regex.regex import Regex


class Unary(Regex):
    """
    Abstract Unary Regular Expressions.
    """
    item = None
    operator = None

    def __init__(self, item):
        self.item = item

    def to_string(self):
        """
        Renders a string, parenthesizing the substring as needed.
        """
        substring = self.item.to_string()
        if len(substring) > 1:
            # TODO: Remove redundant parens.
            return '(' + substring + ')' + self.operator
        else:
            return substring + self.operator
