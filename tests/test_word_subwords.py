from dehns_algorithm import Character, Word


def test_sub_words():
    characters = [Character("a", 1), Character("b", -1)]
    word = Word(characters)
    sub_words = word.sub_words()
    expected_sub_words = [
        Word([]),
        Word([Character("a", 1)]),
        Word([Character("b", -1)]),
        Word([Character("a", 1), Character("b", -1)]),
    ]
    assert sub_words == expected_sub_words
