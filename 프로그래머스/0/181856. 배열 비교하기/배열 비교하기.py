def solution(arr1, arr2):
    answer = 0
    if len(arr1) == len(arr2):
        a1 = 0
        a2 = 0
        for i in arr1: a1 += i
        for i in arr2: a2 += i
        if a2 > a1 : return -1
        elif a2 == a1: return 0
        else: return 1
    else:
        if len(arr2) > len(arr1): return -1
        elif len(arr2) == len(arr1): return 0
        else: return 1