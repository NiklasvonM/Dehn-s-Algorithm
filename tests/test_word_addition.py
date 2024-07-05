from dehns_algorithm import Character, Word


def test_word_add():
    characters1 = [Character("a", 1), Character("b", -1)]
    characters2 = [Character("c", 1), Character("d", -1)]
    word1 = Word(characters1)
    word2 = Word(characters2)
    result = word1 + word2
    assert result.characters == [
        Character("a", 1),
        Character("b", -1),
        Character("c", 1),
        Character("d", -1),
    ]
