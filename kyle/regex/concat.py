"""
Concatenation.
"""
from kyle.fsa.nfa.epsilon_transition import EpsilonTransition
from kyle.regex.binary import Binary


class Concat(Binary):
    """
    Concatenation of two Regular Expressions.
    """
    operator = ''
    _parens = False

    def compile(self):
        """
        Compiles into an NFA by compiling each component regular
        expression and adding EpsilonTransitions from each accept
        state in the left to each initial state in the right NFA.
        """
        left_nfa = self.left.compile()
        right_nfa = self.right.compile()

        for left_state in left_nfa.accept_states:
            for right_state in right_nfa.initial_states:
                left_state.transitions.add(
                    EpsilonTransition(
                        destination=right_state
                    )
                )
        left_nfa.accept_states = right_nfa.accept_states
        return left_nfa
