def solution(a, d, included):
    answer = 0
    arr = [] 
    length = len(included)

    for i in range(length):
        value = a + d * i
        arr.append(value)
        if included[i] == True:
            answer += int(arr[i])
            
    return answer