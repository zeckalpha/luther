"""
DFAState.
"""
from kyle.fsa.state import State


class DFAState(State):
    """
    DFAState.
    """
    def delta(self, character):
        """
        Whereas NFAState.delta returns a set of states, DFAState.delta returns
        either a State or None, since a DFA can only be in one state at a
        time.
        """
        # Returns Maybe DFAState
        for transition in self.transitions:
            if transition.accepts(character):
                return transition.destination
        return None
