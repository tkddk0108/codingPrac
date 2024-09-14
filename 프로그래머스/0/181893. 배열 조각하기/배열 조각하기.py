def solution(arr, query):
    answer = []
    for i in range(len(query)):
        q = query[i]
        if i % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
            
    return arr