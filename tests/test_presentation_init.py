import pytest

from dehns_algorithm import Character, Presentation, Word


def test_presentation_initialization_valid():
    generators = ["a", "b"]
    relators = [Word([Character("a", 1), Character("b", -1)])]
    pres = Presentation(generators, relators)
    assert pres.generators == generators
    assert pres.relators == relators


def test_presentation_initialization_invalid():
    generators = ["a", "b"]
    relators = [Word([Character("c", 1), Character("d", -1)])]
    with pytest.raises(ValueError, match="Letter c is not a generator."):
        Presentation(generators, relators)
