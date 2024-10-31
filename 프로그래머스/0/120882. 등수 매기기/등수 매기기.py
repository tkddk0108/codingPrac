def solution(score):
    answer = []
    result = []
    for i in score:
        answer.append((i[0]+i[1])/2 - 100)
    static = sorted(answer, reverse = True)
    print(answer)
    print(static)
    for i in range(len(answer)):
        for j in range(len(static)):
            if answer[i] == static[j]:
                result.append(j+1)
                break
            
    return result