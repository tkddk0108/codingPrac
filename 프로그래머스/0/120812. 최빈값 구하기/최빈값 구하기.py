def solution(array):
    li = [0] * 1001
    answer = []
    last = []
    
    for i in array:
        li[i] += 1
        
    for i in li:
        if i != 0: answer.append(i)
 
    if answer.count(max(answer)) > 1: return -1
    else: return li.index(max(li))