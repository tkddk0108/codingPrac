def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        j = num_list[i]
        while j  != 1:
            if j % 2 == 0:
                j = j/2
                answer += 1
              
            elif j % 2 == 1:
                j = (j-1)/2
                answer += 1
         
    return answer