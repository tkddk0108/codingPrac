def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isdigit():
            answer += i
        else:
            answer += ' '
    answer = list(map(int, answer.split()))
    return sum(answer)