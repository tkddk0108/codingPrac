def solution(arr):
    answer = []
    two = []
    for i in range(len(arr)):
        if arr[i] == 2: 
            two.append(i)
    
    if len(two) == 0:
        return [-1]
    elif len(two) == 1:

        return arr[two[0]:two[0]+1]
    elif len(two) >= 2:
        a = two[0]
        b = two[-1] + 1
        return arr[a:b]