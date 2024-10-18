def solution(my_string, num1, num2):
    tmp = ''
    answer = ''
    my_string = [x for x in my_string]
    tmp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = tmp
    for x in my_string:
        answer += x
    return answer