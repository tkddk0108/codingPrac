from itertools import permutations
def check(k, du):
    count=0
    for game in du:
        #print(k, du, game)
        if game[0] <= k:
            count += 1 
            k -= game[1]
    #print(count)
    return count

def solution(k, dungeons):
    answer = []
    all = list(permutations(dungeons, len(dungeons)))
    #print(all)
    for i in all:
        #print(k,i)
        answer.append(check(k, i))
    return max(answer)