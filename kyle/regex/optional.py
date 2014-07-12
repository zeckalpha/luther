"""
Optional.
"""
from kyle.regex.unary import Unary


class Optional(Unary):
    """
    Accepts either the empty string or the component Regular Expression.
    """
    operator = '?'

    def compile(self):
        """
        Compile the component Regular Expression and accept any initial state.
        """
        nfa = self.item.compile()
        nfa.accept_states |= nfa.initial_states
        return nfa
