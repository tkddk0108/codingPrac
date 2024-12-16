def TenToThree(n):
    three = ''
    for i in range(18):
        if n < 3**i: 
            maxi = i
            break
    for i in range(maxi-1, -1, -1):
        if n - 2*(3**i) >= 0: 
            three += '2'
            n -= 2*(3**i) 
        elif n - 3**i >= 0: 
            three += '1'
            n -= 3**i
        else: three += '0'
    return three

def ThreeToTen(n):
    answer = 0
    maxi = len(n)-1
    for i in range(len(n)):
        if n[i] == '2':
            answer += 2*(3**maxi)
        elif n[i] == '1':
            answer += 3**maxi
        maxi -= 1
    return answer
        
def solution(n):
    answer = 0
    n = TenToThree(n)
    n = n[::-1]
    return ThreeToTen(n)
