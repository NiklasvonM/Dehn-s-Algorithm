from typing import Literal, Self

INVERTION_EXPONENT_STRING = "\u207b\u00b9"


class Character:
    letter: str
    sign: Literal[-1, 1]

    def __init__(self, letter: str, sign: Literal[-1, 1]) -> None:
        self.letter = letter
        self.sign = sign

    def __str__(self) -> str:
        return self.letter + ("" if self.sign == 1 else INVERTION_EXPONENT_STRING)

    def invert(self) -> Self:
        return Character(self.letter, -1 * self.sign)

    def __eq__(self, other: Self) -> bool:
        return self.letter == other.letter and self.sign == other.sign

    def is_inverse(self, other: Self) -> bool:
        return self.letter == other.letter and self.sign != other.sign
