def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp.lower() or i == alp.upper():
            answer += alp.upper()
        else:
            answer += i
    return answer