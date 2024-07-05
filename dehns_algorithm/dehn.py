from .presentation import Presentation
from .word import Word


def dehn(presentation: Presentation, word: Word) -> list[Word]:
    return _dehn_acc(presentation=presentation, word_list=[word.free_reduce()])


def _dehn_acc(presentation: Presentation, word_list: list[Word]):
    word_cur = word_list[-1]
    if len(word_cur) == 0:
        return word_list
    sublists_word_cur = word_cur.sub_words()
    # is v prefix of some relator? r = v * u
    for v in sublists_word_cur:
        for rel in presentation.relators:
            sublists_relation_cur = rel.sub_words()
            if v not in sublists_relation_cur:
                continue
            # length of v must be less than half of the relator's length
            if len(v) <= len(rel) / 2.0:
                continue
            # delete v from r to get u
            start_ind = None
            for i in range(len(rel)):
                if Word(rel[i : i + len(v)]) == v:
                    start_ind = i
                    break
            u = Word(
                [
                    x
                    for i, x in enumerate(rel)
                    if start_ind is None or not (start_ind <= i < (start_ind + len(v)))
                ]
            )

            # delete v and replace by u^-1
            for i in range(len(rel)):
                if Word(rel[i : i + len(v)]) == v:
                    start_ind = i
                    break
            word_cur = Word(
                [
                    x
                    for i, x in enumerate(word_cur)
                    if start_ind is None or not (start_ind <= i < (start_ind + len(v)))
                ]
            )
            word_cur.characters[start_ind:start_ind] = u.invert_letters()
            word_list.append(word_cur.free_reduce())
            return _dehn_acc(presentation=presentation, word_list=word_list)
    return word_list
