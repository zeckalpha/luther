"""
Union.
"""
from kyle.regex.binary import Binary


class Union(Binary):
    """
    Accept anything either the left or the the right Regular Expression
    accepts.
    """
    operator = '|'

    def compile(self):
        """
        Compile each component Regular Expression and union their initial and
        accept states.
        """
        left_nfa = self.left.compile()
        right_nfa = self.right.compile()
        left_nfa.initial_states |= right_nfa.initial_states
        left_nfa.accept_states |= right_nfa.accept_states
        return left_nfa
