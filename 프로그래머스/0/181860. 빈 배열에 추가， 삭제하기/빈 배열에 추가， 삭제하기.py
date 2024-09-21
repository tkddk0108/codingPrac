def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                answer.append(arr[i])

        else:
            answer = answer[:len(answer)-arr[i]]
    return answer