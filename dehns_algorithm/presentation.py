from .word import Word

EMPTY_SET_STRING = "\u2205"


class Presentation:
    generators: list[str]
    relators: list[Word]

    def __init__(self, generators: list[str], relators: list[Word]) -> None:
        """
        generators: list of strings
        relators: list of words
        words are a list of letters and their formal inverses
        represented by two-element lists containing a letter and a -1 or 1, depending on the sign
        all letters used in the relators need to be generators
        """
        for rel in relators:
            for word in rel:
                if word.letter not in generators:
                    raise ValueError(f"Letter {word} is not a generator.")

        self.generators = generators
        self.relators = relators

    def __str__(self) -> str:
        generators_string = (
            EMPTY_SET_STRING if len(self.generators) == 0 else ", ".join(self.generators)
        )
        relators_string = (
            EMPTY_SET_STRING
            if len(self.relators) == 0
            else ", ".join(str(rel) for rel in self.relators)
        )
        string = "<" + generators_string + " | " + relators_string + ">"
        return string
