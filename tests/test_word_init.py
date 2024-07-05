from dehns_algorithm import Character, Word


def test_word_initialization():
    characters = [Character("a", 1), Character("b", -1)]
    word = Word(characters)
    assert word.characters == characters
