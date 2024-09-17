def solution(arr):
    answer = []
    for i in range(len(arr)):
        x = arr[i]
        for j in range(x):
            answer.append(arr[i])
    return answer