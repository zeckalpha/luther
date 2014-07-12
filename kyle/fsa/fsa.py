"""
Finite State Automaton.
"""


class FSA(object):
    """
    Abstract Finite State Automaton.
    """
    def accepts(self, string):
        """
        FSAs can accept or reject strings.
        """
        raise NotImplementedError
