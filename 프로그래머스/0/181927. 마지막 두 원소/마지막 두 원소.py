def solution(num_list):
    answer = []
    a = len(num_list)
    
    if num_list[a-2] < num_list[a-1]:
        value = num_list[a-1] - num_list[a-2]
        num_list.append(value)
        
    elif num_list[a-2] >= num_list[a-1]:
        value = num_list[a-1] * 2
        num_list.append(value)
        
    return num_list