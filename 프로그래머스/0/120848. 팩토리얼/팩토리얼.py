def solution(n):
    answer = 0
    if n == 1: return 1
    for i in range(1, 11):
        for j in range(1, i+1):
            if j == 1: val = i * j
            else: val *= j
        if val > n : return i
