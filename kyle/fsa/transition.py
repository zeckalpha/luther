"""
Transition.
"""


class Transition(object):
    """
    A transition has a function called accepts which decides whether to follow
    the transition, and a destination state to take if decided.
    """
    destination = None  # A State  # TODO: Assert
    accepts = None  # Character -> Boolean

    def __init__(self, accepts, destination):
        self.accepts = accepts
        self.destination = destination
