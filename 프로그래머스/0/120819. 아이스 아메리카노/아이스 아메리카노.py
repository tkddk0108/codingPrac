def solution(money):
    answer = []
    for i in range(190):
        if money < 5500:
            answer = [0, money]
            return answer
        elif money - 5500*i == 0:
            answer = [i, money - 5500*i]
            return answer
        elif money - 5500*i <= 0:
            answer =  [i-1, money - 5500*(i-1)]
            return answer
