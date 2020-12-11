import copy

def free_reduce(word):
    res = copy.deepcopy(word)
    i = 0
    while i < len(res)-1:
        if res[i][0] == res[i+1][0] and res[i][1] != res[i+1][1]:
            del res[i:i+2]
            i = max(0, i-2)
        i = i+1
    return res


class presentation:

    # generators: list of strings
    # relators: list of words
    # words are a list of letters and their formal inverses
    # represented by two-element lists containing a letter and a -1 or 1, depending on the sign
    # all letters used in the relators need to be generators
    def __init__(self, generators, relators):
        # Input checks
        for rel in relators:
            for letter in rel:
                if letter[0] not in generators:
                    raise ValueError("Letter " + letter + " is not a generator.")
                if letter[1] not in [-1, 1]:
                    raise ValueError("Sign must be -1 or 1. Is " + letter[1] + " for letter " + letter[0] + ".")

        self.generators = generators
        self.relators = relators

    # Override print()
    def __str__(self):
        if len(self.generators) == 0:
            strGens = "\u2205" # empty set
        else:
            strGens = ', '.join(self.generators)
        if len(self.relators) == 0:
            strRels = "\u2205" # empty set
        else:
            strRels = ', '.join(
                [''.join(
                    [letter[0] + ('' if letter[1] == 1 else '\u207b\u00b9') for letter in rel]
                ) for rel in self.relators]
            )
        print(strRels)
        string = "<" + strGens + " | " + strRels + ">"
        return string

# presentation for Z^2
pres = presentation(
    ["a", "b"],
    [
        [
            ["a", 1],
            ["b", 1],
            ["a", -1],
            ["b", -1]
        ]
    ]
)
print(pres)
