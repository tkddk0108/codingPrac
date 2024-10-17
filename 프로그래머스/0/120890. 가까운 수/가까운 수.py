def solution(array, n):
    array = sorted(array)
    answer = array[0]
    cha = n-array[0]

    for i in array:
        if abs(n-i) < cha:
            cha = abs(n-i)
            answer = i
        
    return answer