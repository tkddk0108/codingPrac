def solution(sizes):
    answer = 0
    b, s = [], []
    for card in sizes:
        b.append(max(card))
        s.append(min(card))
    
    return max(b) * max(s)