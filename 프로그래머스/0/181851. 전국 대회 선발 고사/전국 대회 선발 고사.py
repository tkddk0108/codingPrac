def solution(rank, attendance):
    answer = []
    for idx, ranking in enumerate(rank):
        if attendance[idx] == True:
            answer.append([idx,ranking])
            
    answer.sort(key=lambda x: x[1])
    print(answer[0][0]*100)
    print(answer[1][0]*100)
    print(answer[2][0])
    return answer[0][0]*10000 + answer[1][0]*100 + answer[2][0]