"""
Plus.
"""
from kyle.regex.unary import Unary
from kyle.regex.concat import Concat
from kyle.regex.star import Star


class Plus(Unary):
    """
    Accepts one or more of the component Regular Expression.
    """
    operator = '+'

    def compile(self):
        """
        Concatenate the component Regular Expression with the Starred component
        Regular Expression.
        """
        return Concat(self.item, Star(self.item)).compile()
