def solution(arr, queries):
    answer = []
    length=len(queries)
    
    for i in range(length):
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]
        
        for a in range(s, e+1):
            if a % k == 0:
                arr[a] += 1

    answer = arr
    return answer