def solution(n, arr1, arr2):
    answer = []
    arr1, arr2 = [], []
    for i in arr1:
        row = [0]*5
        for j in range (n-1, 0, -1):
            if i - 2^j >= 0:
                row[n] = 1
            else: 
                row[n] = 0
        arr1.append[row]
    print(arr1)
    return answer