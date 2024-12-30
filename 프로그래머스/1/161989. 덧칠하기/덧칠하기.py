def solution(n, m, section):
    answer = 0
    result = [0] * n
    for i in section:
        result[i-1] = 1
    for i in range(len(result)):
        if result[i] == 1:
            answer += 1
            mini = min(i+m, len(result))
            for j in range(i, mini):
                result[j] = 0
    return answer