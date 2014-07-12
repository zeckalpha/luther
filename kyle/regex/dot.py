"""
Dot.
"""

from kyle.regex.character import Character


class InfiniteSet(set):
    """
    The set containing everything.
    """
    def __contains__(self, other):
        return True


class Dot(Character):
    """
    The Character class which accepts all inputs.
    """
    # TODO: Use in Regex.from_string.
    characters = InfiniteSet()

    def to_string(self):
        return '.'
