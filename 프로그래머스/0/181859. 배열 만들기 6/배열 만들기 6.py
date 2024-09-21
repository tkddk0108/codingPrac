def solution(arr):
    answer = []
    i=0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
        elif answer != [] and answer[-1] == arr[i]:
            answer.pop()
        elif answer != [] and answer[-1] != arr[i]:
            answer.append(arr[i])
        i += 1
    if answer == [] : return [-1]
    else: return answer