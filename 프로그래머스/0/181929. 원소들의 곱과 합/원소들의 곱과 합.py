def solution(num_list):
    answer = 0
    mul = 1
    squ = 0
    sum = 0
    
    for i in range(len(num_list)):
        mul *= num_list[i]
        sum += num_list[i]
    squ = sum*sum
    
    if mul < squ: answer = 1
    elif mul > squ: answer = 0
    
    return answer