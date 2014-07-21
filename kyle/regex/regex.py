"""
Regular Expressions.
"""


class Regex(object):
    """
    Regular Expressions.
    """
    @classmethod
    def from_string(cls, string):
        """
        Construct a Regex from a given string representation.
        """
        return cls.from_infix(string)

    @classmethod
    def from_infix(cls, string):
        """
        Construct a Regex from an infix string representation.
        """
        return cls.from_postfix(cls._string_to_postfix(string))

    @classmethod
    def from_postfix(cls, postfix):
        """
        Construct a Regex from a postfix representation.
        """
        from kyle.regex.optional import Optional
        from kyle.regex.star import Star
        from kyle.regex.plus import Plus
        from kyle.regex.union import Union
        from kyle.regex.concat import Concat
        from kyle.regex.character import Character

        # stack is just a list
        unary = {
            '?': Optional,
            '*': Star,
            '+': Plus
        }
        binary = {
            '|': Union,
            '.': Concat  # TODO: Dot?
        }
        stack = []
        for character in postfix:
            if character in unary:
                try:
                    previous = stack.pop()
                except IndexError:
                    raise SyntaxError
                stack.append(
                    unary[character](previous)
                )
            elif character in binary:
                try:
                    right = stack.pop()
                    left = stack.pop()
                except IndexError:
                    raise SyntaxError
                stack.append(
                    binary[character](left, right)
                )
            else:
                stack.append(
                    Character(character)
                )
        assert len(stack) == 1
        return stack.pop()

    @classmethod
    def _string_to_postfix(cls, string):
        """
        Parses the regular expression into postfix form.

        See re2post: http://swtch.com/~rsc/regexp/nfa.c.txt
        """
        # TODO: Off by one errors.
        # TODO: Escapes.
        # TODO: Periods.
        postfix = ''
        unary = {
            "*",
            "+",
            "?"
        }
        stack = []
        literals = 0
        alternates = 0

        for character in string:
            if character == "(":
                if literals > 1:
                    literals -= 1
                    postfix += "."
                stack.append((literals, alternates))
                literals = 0
                alternates = 0
            elif character == "|":
                if literals == 0:
                    raise SyntaxError
                while literals > 1:
                    postfix += "."
                    literals -= 1
                literals = 0
                alternates += 1
            elif character == ")":
                if literals == 0:
                    raise SyntaxError
                while literals > 1:
                    postfix += "."
                    literals -= 1
                literals = 0
                while alternates:
                    postfix += "|"
                    alternates -= 1
                try:
                    literals, alternates = stack.pop()
                except IndexError:
                    raise SyntaxError
                literals += 1
            # The unary operators are already postfix
            elif character in unary:
                if literals == 0:
                    raise SyntaxError
                postfix += character
            # A literal character
            else:
                # concatenate more than two literal characters
                if literals > 1:
                    literals -= 1
                    postfix += "."
                postfix += character
                literals += 1
        if len(stack) > 0:
            raise SyntaxError
        while literals > 1:
            postfix += "."
            literals -= 1
        literals = 0
        while alternates:
            postfix += "|"
            alternates -= 1
        return postfix

    def to_string(self):
        """
        Abstract. Return a string representation of the Regex.
        """
        raise NotImplementedError

    def compile(self):
        """
        Abstract compile method. Return an NFA.
        """
        raise NotImplementedError

    def accepts(self, string):
        """
        Convenience method for one-off Regexs.
        """
        return self.compile().accepts(string)
