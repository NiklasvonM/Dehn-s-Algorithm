from __future__ import annotations

import copy

from .character import Character


class Word:
    characters: list[Character]

    def __init__(self, characters: list[Character]) -> None:
        self.characters: list[Character] = characters

    def invert_letters(self) -> Word:
        """Inverts the letters sequentially. Does not invert the word itself."""
        inverted_characters = [character.invert() for character in self.characters]
        return Word(characters=inverted_characters)

    def __str__(self) -> str:
        return "".join(str(character) for character in self.characters)

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, index: int) -> Character:
        return self.characters[index]

    def __len__(self) -> int:
        return len(self.characters)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Word):
            return self.characters == other.characters
        return False

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __add__(self, other: object) -> Word:
        if isinstance(other, Word):
            return Word(self.characters + other.characters)
        return NotImplemented

    def free_reduce(self) -> Word:
        result = copy.deepcopy(self)
        i = 0
        while i < len(result) - 1:
            character_current = result[i]
            character_next = result[i + 1]
            if character_current.is_inverse(character_next):
                del result.characters[i : i + 2]
                i = -1  # start at the beginning of the list again
            i += 1
        return result

    def sub_words(self) -> list[Word]:
        """Generates all subwords of the current word.

        Returns:
            A list of Word objects representing all possible subwords.
        """

        sub_words_list: list[Word] = [Word([])]  # Start with an empty subword

        for character in self.characters:
            new_sub_words: list[Word] = []
            for existing_sub_word in sub_words_list:
                extended_sub_word = existing_sub_word + Word([character])
                new_sub_words.append(extended_sub_word)
            sub_words_list.extend(new_sub_words)  # Add the new subwords

        return sub_words_list
