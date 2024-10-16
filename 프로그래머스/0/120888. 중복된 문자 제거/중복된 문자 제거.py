def solution(my_string):
    answer = ''
    li = [i for i in my_string]
    for i in li:
        if i not in answer: answer += i
    return answer