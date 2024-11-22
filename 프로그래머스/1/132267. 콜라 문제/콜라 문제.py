def solution(a, b, n):
    cnt = 0
    remain = n
    while remain >= a:
        remain -= a
        remain += b
        cnt += b
    return cnt