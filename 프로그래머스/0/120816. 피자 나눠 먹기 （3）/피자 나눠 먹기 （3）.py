def solution(s, n):
    for i in range(s, s*100, s):
        if i // n >= 1:
            return i // s
