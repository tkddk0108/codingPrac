def solution(arr):
    answer = [arr[0]]

    for n in range(1, len(arr)):
        if arr[n] != answer[-1]:
            answer.append(arr[n])
    return answer