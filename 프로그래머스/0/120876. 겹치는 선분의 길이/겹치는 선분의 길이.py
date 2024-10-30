def solution(lines):
    answer = 0
    value = []

    for i in lines:
        start = i[0]
        end = i[1]
        
        for j in range(i[1] - i[0]):
            if start == end:
                continue
            
            pair = [start, start+1]
        
            if pair in value:
                answer+=1
                value.remove(pair)
            else:
                value.append(pair)
            
            start += 1
            
    return answer