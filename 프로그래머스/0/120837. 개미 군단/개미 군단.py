def solution(hp):
    answer = 0
    while hp != 0:
        if hp - 5 >= 0:
            answer += 1
            hp -= 5
        elif hp - 3 >= 0:
            answer += 1
            hp -= 3
        elif hp - 1 >= 0:
            answer += 1
            hp -= 1
    return answer