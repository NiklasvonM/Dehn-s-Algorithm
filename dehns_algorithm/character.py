from __future__ import annotations

from typing import Literal, cast

INVERTION_EXPONENT_STRING = "\u207b\u00b9"


class Character:
    letter: str
    sign: Literal[-1, 1]

    def __init__(self, letter: str, sign: Literal[-1, 1]) -> None:
        self.letter = letter
        self.sign = sign

    def __str__(self) -> str:
        return self.letter + ("" if self.sign == 1 else INVERTION_EXPONENT_STRING)

    def invert(self) -> Character:
        inverted_sign: Literal[-1, 1] = cast(Literal[-1, 1], -1 * self.sign)
        return Character(self.letter, inverted_sign)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Character):
            return self.letter == other.letter and self.sign == other.sign
        return False

    def is_inverse(self, other: Character) -> bool:
        return self.letter == other.letter and self.sign != other.sign
