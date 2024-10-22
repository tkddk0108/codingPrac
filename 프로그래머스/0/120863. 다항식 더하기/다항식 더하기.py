def solution(polynomial):
    answer = ''
    li = list(map(str, polynomial.split()))
    x, num = 0,0
    for i in li:
        if 'x' in i:
            if len(i) == 1: x += 1
            else: x += int(i[:len(i)-1])
        elif i == '+':
            continue
        else:
            num += int(i)
    if x!=0 and num != 0:
        answer = f'{x}x + {num}'
    elif x != 0 and num == 0:
        answer = f'{x}x'
    elif num != 0 and x == 0:
        answer = str(num)
        
    if f'{x}x' == '1x':
        answer = answer.replace('1x', 'x')
    return answer