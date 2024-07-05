from dehns_algorithm import Character


def test_character_initialization():
    char = Character("a", 1)
    assert char.letter == "a"
    assert char.sign == 1

    char = Character("b", -1)
    assert char.letter == "b"
    assert char.sign == -1
