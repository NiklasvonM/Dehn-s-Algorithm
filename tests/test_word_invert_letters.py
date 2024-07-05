from dehns_algorithm import Character, Word


def test_invert_letters():
    characters = [Character("a", 1), Character("b", -1)]
    word = Word(characters)
    inverted_word = word.invert_letters()

    assert inverted_word.characters == [Character("a", -1), Character("b", 1)]
    assert word.characters == characters  # Original word should not be modified
