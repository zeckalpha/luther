"""
Character.
"""
import string

from kyle.fsa.nfa.nfa import NFA
from kyle.fsa.nfa.nfa_state import NFAState
from kyle.fsa.transition import Transition
from kyle.regex.regex import Regex


class Character(Regex):
    """
    A character or character class regular expression. Consumes one character
    from the input.
    """
    characters = ''

    def __init__(self, characters):
        self.characters = characters

    def compile(self):
        """
        Constructs an NFA by creating two states with one transition that
        accepts only if the character considered is in self.characters.
        """
        initial_state = NFAState()
        accept_state = NFAState()
        initial_state.transitions.add(
            Transition(
                accepts=lambda character: character in self.characters,
                destination=accept_state
            )
        )
        return NFA(
            initial_states={initial_state},
            accept_states={accept_state},
        )

    def to_string(self):
        """
        A single character, or a [character class].
        """
        if len(self.characters) == 1:
            return self.characters
        else:
            return '[' + self.characters + ']'


# TODO: Use character classes in Regex.from_postfix.

Digits = Character(string.digits)
HexDigits = Character(string.hexdigits)
Letters = Character(string.letters)
Lowercase = Character(string.lowercase)
OctDigits = Character(string.octdigits)
Punctuation = Character(string.punctuation)
Printable = Character(string.printable)
Uppercase = Character(string.uppercase)
Whitespace = Character(string.whitespace)
