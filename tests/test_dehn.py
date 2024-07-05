from dehns_algorithm import Character, Presentation, Word, dehn


def test_z2():
    # presentation for Z^2
    presentation = Presentation(
        ["a", "b"],
        [Word([Character("a", 1), Character("b", 1), Character("a", -1), Character("b", -1)])],
    )

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
    expected = [
        Word(
            [
                Character("a", -1),
                Character("b", 1),
                Character("a", -1),
                Character("b", -1),
                Character("a", 1),
                Character("a", 1),
            ]
        ),
        Word([]),
    ]
    assert dehn(presentation, word) == expected


def test_dehn_no_reduction():
    """Test that Dehn's algorithm leaves a non-reducible word unchanged."""
    presentation = Presentation(
        ["x", "y"],
        [Word([Character("x", 1), Character("y", 1)])],  # No inverse
    )
    word = Word([Character("x", 1), Character("y", -1)])
    assert dehn(presentation, word) == [word]


def test_dehn_empty_word():
    """Test that Dehn's algorithm returns an empty list for an empty word."""
    presentation = Presentation(["a", "b"], [])
    word = Word([])
    assert dehn(presentation, word) == [word]
