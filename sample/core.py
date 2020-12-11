

class word:

    def __init__(self, letters, presentation):
        pass



class presentation:

    def __init__(self, generators, relators):
        for rel in relators:
            for letter in rel:
                if letter[0] not in generators:
                    raise ValueError("Letter " + letter + " is not a generator.")
                if letter[1] not in [-1, 1]:
                    raise ValueError("Sign must be -1 or 1. Is " + letter[1] + " for letter " + letter[0] + ".")
        self.generators = generators
        self.relators = relators

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
