from itertools import combinations

def solution(nums):
    prime = []
    for i in combinations(nums, 3):
        prime.append(sum(i))
    answer = len(prime)
    #print(prime)
    for i in prime:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                answer -= 1
                break
    return answer