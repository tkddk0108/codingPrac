def solution(arr, queries):
    answer = []
    box=0
    for i in range(len(queries)):
        a = queries[i][0]   #0
        b = queries[i][1]   #3
        box = arr[b] #arr[3]
        arr[b]=arr[a]
        arr[a]=box
        answer = arr
    return answer