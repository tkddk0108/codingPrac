from collections import Counter

def solution(k, tangerine):
    answer, s = 0, 0
    a = Counter(tangerine)
    sort_t = sorted(a.values(),reverse=True)

    while k > 0:
        k -= sort_t[s]
        answer += 1
        s += 1
    return answer