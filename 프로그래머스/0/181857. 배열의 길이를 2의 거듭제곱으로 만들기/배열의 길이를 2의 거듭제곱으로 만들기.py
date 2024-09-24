def solution(arr):
    answer = []
    length = []
    for i in range(12):
        length.append(2**i)
    for i in range(len(length)):
        if len(arr) > length[i] and len(arr) < length[i+1]:
            for j in range(length[i+1]): #8
                if len(arr) > j: answer.append(arr[j])
                else: answer.append(0)
            return answer
        elif len(arr) in length:
            return arr
