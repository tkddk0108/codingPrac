def solution(common):
    if common[0] - common[1] == common[1] - common[2]:
        return common[-1] +(common[1]-common[0])
    elif common[2] // common[1] == common[1] // common[0]:
        return common[-1] * (common[2] //common[1])
    #return answer