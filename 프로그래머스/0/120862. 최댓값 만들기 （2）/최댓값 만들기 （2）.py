def solution(numbers):
    answer = 0
    li = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            li.append(numbers[i]*numbers[j])
            # print(numbers[i]*numbers[j])
    return max(li)