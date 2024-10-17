def solution(order):
    answer = 0
    order = str(order)
    tsn = ['3','6','9']
    
    for i in order:
        print(i)
        if i in tsn: answer += 1
        
    return answer