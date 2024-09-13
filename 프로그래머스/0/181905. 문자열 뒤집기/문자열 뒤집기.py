def solution(my_string, s, e):
    answer = ''
    re = my_string[s:e+1]
    answer = my_string[:s] + re[::-1] + my_string[e+1:]
    return answer