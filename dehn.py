import copy
from pprint import pprint
from typing import Literal

Word = list[tuple[str, Literal[-1, 1]]]


def free_reduce(word: Word) -> Word:
    res = copy.deepcopy(word)
    i = 0
    while i < len(res) - 1:
        if res[i][0] == res[i + 1][0] and res[i][1] != res[i + 1][1]:
            del res[i : i + 2]
            i = -1
        i = i + 1
    return res


def sub_lists(l: list) -> list[list]:
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists
    return lists


def invert_word(word: Word) -> Word:
    return [[letter[0], -1 * letter[1]] for letter in word]


class Presentation:
    def __init__(self, generators: list[str], relators: list[Word]):
        """
        generators: list of strings
        relators: list of words
        words are a list of letters and their formal inverses
        represented by two-element lists containing a letter and a -1 or 1, depending on the sign
        all letters used in the relators need to be generators
        """
        # Input checks
        for rel in relators:
            for letter in rel:
                if letter[0] not in generators:
                    raise ValueError("Letter " + letter + " is not a generator.")
                if letter[1] not in [-1, 1]:
                    raise ValueError(
                        "Sign must be -1 or 1. Is "
                        + letter[1]
                        + " for letter "
                        + letter[0]
                        + "."
                    )

        self.generators: list[str] = generators
        self.relators: list[Word] = relators

    def __str__(self):
        if len(self.generators) == 0:
            strGens = "\u2205"  # empty set
        else:
            strGens = ", ".join(self.generators)
        if len(self.relators) == 0:
            strRels = "\u2205"  # empty set
        else:
            strRels = ", ".join(
                [
                    "".join(
                        [
                            letter[0] + ("" if letter[1] == 1 else "\u207b\u00b9")
                            for letter in rel
                        ]
                    )
                    for rel in self.relators
                ]
            )
        # print(strRels)
        string = "<" + strGens + " | " + strRels + ">"
        return string

    def dehn(self, word):
        return self.__dehn_acc([free_reduce(word)])

    def __dehn_acc(self, w_seq: list[Word]):
        w_cur = w_seq[-1]
        if len(w_cur) == 0:
            return w_seq
        # is v prefix of some relator? r = v * u
        for v in sub_lists(w_cur):
            for rel in self.relators:
                if v in sub_lists(rel):
                    # length of v must be less than half of the relator's length
                    if len(v) > len(rel) / 2.0:
                        # delete v from r to get u
                        start_ind = None
                        for i in range(len(rel)):
                            if rel[i : i + len(v)] == v:
                                start_ind = i
                                break
                        u = [
                            x
                            for i, x in enumerate(rel)
                            if start_ind is None
                            or not (start_ind <= i < (start_ind + len(v)))
                        ]

                        # delete v and replace by u^-1
                        for i in range(len(rel)):
                            if rel[i : i + len(v)] == v:
                                start_ind = i
                                break
                        w_cur = [
                            x
                            for i, x in enumerate(w_cur)
                            if start_ind is None
                            or not (start_ind <= i < (start_ind + len(v)))
                        ]

                        # print("v = " + str(v))
                        # print("rel = " + str(rel))
                        # print("u = " + str(u))
                        # print("w_cur = " + str(w_cur))
                        w_cur[start_ind:start_ind] = invert_word(u)
                        # print("w_cur = " + str(w_cur))
                        w_seq.append(free_reduce(w_cur))
                        # print("w_seq = " + str(w_seq))
                        return self.__dehn_acc(w_seq)
        return w_seq


def main():
    # presentation for Z^2
    pres = Presentation(
        ["a", "b"], [[(["a", 1]), (["b", 1]), (["a", -1]), (["b", -1])]]
    )
    print("Presentation for Z^2:")
    print(pres)

    word: list[tuple[str, Literal[-1, 1]]] = [
        ("a", -1),
        ("b", 1),
        ("a", -1),
        ("b", -1),
        ("a", 1),
        ("b", -1),
        ("b", 1),
        ("a", 1),
    ]
    print("Word:")
    pprint(word)
    print("Reduced word:")
    pprint(pres.dehn(word))


if __name__ == "__main__":
    main()
