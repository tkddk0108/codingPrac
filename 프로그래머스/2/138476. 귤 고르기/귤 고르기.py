from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    count = sorted(counter.values(), reverse = True)
    s = 0
    while k > 0:
        k -= count[s]
        answer += 1
        s += 1
    
    return answer