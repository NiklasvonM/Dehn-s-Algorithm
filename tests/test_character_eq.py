from dehns_algorithm import Character


def test_character_eq():
    char1 = Character("a", 1)
    char2 = Character("a", 1)
    assert char1 == char2

    char3 = Character("a", -1)
    assert char1 != char3  # Different signs


def test_character_is_inverse():
    char1 = Character("a", 1)
    char2 = Character("a", -1)
    assert char1.is_inverse(char2)
    assert char2.is_inverse(char1)
