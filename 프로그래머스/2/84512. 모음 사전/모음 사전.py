def solution(word):
    answer = 0
    words = []
    for a in "AEIOU":
        words.append(a)
        for b in "AEIOU":
            words.append(a+b)
            for c in "AEIOU":
                words.append(a+b+c)
                for d in "AEIOU":
                    words.append(a+b+c+d)
                    for e in "AEIOU":
                        words.append(a+b+c+d+e)
    return words.index(word)+1