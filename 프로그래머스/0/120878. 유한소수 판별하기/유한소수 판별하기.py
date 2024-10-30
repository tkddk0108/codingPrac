def solution(a, b):
    answer = 0
    for i in range(b, 2, -1):
        if a%i==0 and b%i==0:
            a = a//i
            b = b//i
            i = 2
    for j in range(200):
        if b % 2 == 0: b = b//2
        elif b % 5 == 0: b = b//5
        elif b != 1:
            return 2
    return 1