def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        idx = int(index_list[i])
        answer += my_string[idx]
    
    return answer