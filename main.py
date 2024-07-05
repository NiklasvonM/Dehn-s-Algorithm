from dehns_algorithm import Character, Presentation, Word, dehn


def main():
    # presentation for Z^2
    presentation = Presentation(
        ["a", "b"],
        [Word([Character("a", 1), Character("b", 1), Character("a", -1), Character("b", -1)])],
    )
    print("Presentation for Z^2:")
    print(presentation)

    word = Word(
        [
            Character("a", -1),
            Character("b", 1),
            Character("a", -1),
            Character("b", -1),
            Character("a", 1),
            Character("b", -1),
            Character("b", 1),
            Character("a", 1),
        ]
    )
    print("Word:")
    print(word)
    print("Reduced word:")
    print(dehn(presentation, word))


if __name__ == "__main__":
    main()
