def solution(num_list):
    answer = []
    one = 0
    two = 0
    for i in num_list:
        if i % 2 == 0:
            two += 1
        else:
            one += 1
    answer.append(two)
    answer.append(one)
    return answer