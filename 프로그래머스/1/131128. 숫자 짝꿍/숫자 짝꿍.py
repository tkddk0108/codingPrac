from collections import Counter

def solution(X, Y):
    answer = []
    cY = Counter(Y)

    for i in X:
        if cY[i] != 0:
            answer.append(i)
            cY[i] -= 1
            
    if answer == []: return "-1"
    else: 
        answer = sorted(answer, reverse = True)
        if answer[0] == "0": return "0"
        return ''.join(answer)

