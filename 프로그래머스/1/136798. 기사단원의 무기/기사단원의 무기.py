def check(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if i == n//i:
                count += 1
            else:
                count += 2
    return count

def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(1, number+1):
        arr.append(check(i))
    for i in arr:
        if i<=limit:
            answer += i
        else:
            answer += power
    return answer