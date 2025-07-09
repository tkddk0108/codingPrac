def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        dic = dict(zip(want, number))
        for j in discount[i:i+10]:
            if j in dic.keys():
                dic[j] -= 1
                
        if all(value <= 0 for value in dic.values()):
                answer += 1
    return answer