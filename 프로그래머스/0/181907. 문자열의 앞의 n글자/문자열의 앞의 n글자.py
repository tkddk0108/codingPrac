def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        if i < n:
            answer += my_string[i]
    return answer