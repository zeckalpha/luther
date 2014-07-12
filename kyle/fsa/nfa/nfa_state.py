"""
NFAState.
"""
from kyle.fsa.state import State
from kyle.fsa.nfa.epsilon_transition import EpsilonTransition


class NFAState(State):
    """
    NFAStates can have EpsilonTransitions, which are followed without
    consuming any input, and thus the delta method needs to consider these as
    being equivalent to self.
    """
    def _epsilon_destinations(self):
        """
        Private method.
        """
        for transition in self.transitions:
            if isinstance(transition, EpsilonTransition):
                yield transition.destination

    def delta(self, character):
        """
        Return a set of states which can be reached by consuming the supplied
        character.
        """
        states = {self}
        destinations = set()
        visited = set()
        while states:
            state = states.pop()
            for transition in self.transitions:
                if transition.accepts(character):
                    destinations.add(transition.destination)
            for eps_destination in state._epsilon_destinations():
                if eps_destination not in visited:
                    states.add(eps_destination)
            visited.add(state)
        return destinations
