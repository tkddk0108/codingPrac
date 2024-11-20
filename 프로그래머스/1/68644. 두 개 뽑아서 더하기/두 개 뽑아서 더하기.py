def solution(numbers):
    answer = []
    val = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!= j: val.append(numbers[i] + numbers[j]) 
    
    return sorted(set(val))