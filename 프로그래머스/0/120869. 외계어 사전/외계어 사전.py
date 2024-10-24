def solution(spell, dic):
    answer = 0
    set_spell = set(spell)
    for i in dic:
        word = [x for x in i]
        if set_spell.issubset(set(word)):
            return 1
    return 2