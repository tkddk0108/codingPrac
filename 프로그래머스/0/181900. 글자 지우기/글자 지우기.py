def solution(my_string, indices):
    answer = ''
    indices.sort()
    #print(indices)
    val = []
    for i in range(len(my_string)):
        if i not in indices:
            val += my_string[i]
    #for j in range(len(indices)):
        #val.remove(val[indices[j]])
    for j in range(len(val)):
        answer += val[j]

    return answer