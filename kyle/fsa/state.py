"""
State.
"""


class State(object):
    """
    An FSA has States, which have Transitions amongst themselves.
    """
    transitions = set()

    def __init__(self, transitions=None):
        if transitions:
            self.transitions = transitions
