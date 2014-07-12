"""
Deterministic Finite Automaton.
"""
from kyle.fsa.fsa import FSA


class DFA(FSA):
    """
    Deterministic Finite Automaton.
    """
    initial_state = None
    accept_state = None

    def __init__(self, initial_state, accept_state):
        self.initial_state = initial_state
        self.accept_state = accept_state

    def accepts(self, string):
        """
        Follows the DFA, checking if the supplied string ends in the
        accept_state.
        """
        state = self.initial_state
        for character in string:
            state = state.delta(character)
            if state is None:
                return False
        return state is self.accept_state
