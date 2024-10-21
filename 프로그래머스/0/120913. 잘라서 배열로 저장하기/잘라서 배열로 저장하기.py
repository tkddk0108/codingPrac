def solution(my_str, n):
    answer = []
    for i in range(len(my_str) // n + 1):
        if len(my_str) >= n:
            answer.append(my_str[:n])
            my_str = my_str[n:]
        elif len(my_str) >= 1:
            answer.append(my_str)
        else:
            return answer

    return answer