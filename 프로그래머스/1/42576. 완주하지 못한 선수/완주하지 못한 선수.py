def solution(participant, completion):
    dic = {}
    # dic에 추가하는 과정
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in completion:
        dic[i] -= 1
    
    for i in dic:
        if dic[i] != 0:
            return i