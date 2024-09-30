def solution(arr):
    answer = [[]]
    li = []
    if len(arr) > len(arr[1]):
        for i in range(len(arr)):
            while len(arr[i]) != len(arr):
                arr[i].append(0)
    elif len(arr) < len(arr[1]):
        for i in range(len(arr[0])):
            while len(arr[i]) != len(arr):
                for _ in range(len(arr[0])):
                    li.append(0)
                arr.append(li)
                li = []
    else:
        return arr
    
    return arr