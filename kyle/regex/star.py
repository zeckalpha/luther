"""
Star.
"""
from kyle.fsa.nfa.epsilon_transition import EpsilonTransition
from kyle.regex.unary import Unary
from kyle.regex.optional import Optional


class Star(Unary):
    """
    Zero or more of the component Regular Expression.
    """
    operator = '*'

    def compile(self):
        """
        Compile an Optional of the component Regular Expression, and then add
        EpsilonTransitions from each accept state to each initial state.
        """
        nfa = Optional(self.item).compile()
        for initial_state in nfa.initial_states:
            for accept_state in nfa.accept_states:
                accept_state.transitions.add(
                    EpsilonTransition(
                        destination=initial_state
                    )
                )
        return nfa
