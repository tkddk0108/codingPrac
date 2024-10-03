def solution(n):
    answer = 0
    for i in range(7, 140, 7):
        if i // n >= 1:
            return i//7
    return answer