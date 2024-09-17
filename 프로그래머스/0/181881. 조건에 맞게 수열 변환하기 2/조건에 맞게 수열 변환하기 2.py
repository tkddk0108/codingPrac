def solution(arr):
    answer = []
    n=0
    while answer != arr:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2 == 0: 
                answer.append(int(arr[i]/2))
            elif arr[i] < 50 and arr[i]%2 == 1:
                answer.append(int(arr[i]*2+1))
            else:
                answer.append(arr[i])
        if answer == arr:
            return n
        else:
            n+= 1
            arr = answer
            answer = []
