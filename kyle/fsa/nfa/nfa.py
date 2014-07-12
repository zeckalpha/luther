"""
Non-deterministic Finite Automaton.
"""
from kyle.fsa.fsa import FSA


class NFA(FSA):
    """
    Non-deterministic Finite Automaton.
    """
    initial_states = set()
    accept_states = set()

    def __init__(self, initial_states=None, accept_states=None):
        if initial_states:
            self.initial_states = initial_states
        if accept_states:
            self.accept_states = accept_states

    def accepts(self, string):
        """
        Follows the NFA returning true if one of the end states is an
        accept_state.
        """
        states = self.initial_states
        for character in string:
            next_states = set()
            for state in states:
                next_states |= set(state.delta(character))
            states = next_states
        for state in states:
            if state in self.accept_states:
                return True
        return False
