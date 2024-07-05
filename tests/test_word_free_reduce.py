from dehns_algorithm import Character, Word


def test_free_reduce():
    characters = [Character("a", 1), Character("a", -1), Character("b", 1)]
    word = Word(characters)
    reduced_word = word.free_reduce()
    assert reduced_word.characters == [Character("b", 1)]
