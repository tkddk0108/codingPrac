def solution(my_string, n):
    answer = ''
    string = my_string[::-1]
    answer += string[:n]
    answer = answer[::-1]
    
    return answer