"""
EpsilonTransition.
"""
from kyle.fsa.transition import Transition


class EpsilonTransition(Transition):
    """
    EpsilonTransitions cannot accept anything, since they do not consume any
    input.
    """
    def __init__(self, destination):
        accepts = lambda character: False
        super(EpsilonTransition, self).__init__(accepts, destination)
