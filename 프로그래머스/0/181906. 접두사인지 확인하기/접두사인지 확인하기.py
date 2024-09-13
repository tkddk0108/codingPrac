def solution(my_string, is_prefix):
    answer = 0
    li = []
    for i in range(len(my_string)):
        li.append(my_string[:i+1])
        
    if is_prefix in li:
        answer = 1
    else:
        answer = 0
    return answer