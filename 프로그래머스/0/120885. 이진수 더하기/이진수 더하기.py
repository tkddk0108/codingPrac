def solution(bin1, bin2):
    answer = ''
    one, two, cnt = 0, 0, 1
    if bin1 == '0': return bin2
    elif bin2 == '0': return bin1
    for i in bin1:
        if i == '1':
            one += 2**(len(bin1) - cnt)
        cnt += 1
    
    cnt  = 1
    for i in bin2:
        if i == '1':
            two += 2**(len(bin2) - cnt)
        cnt += 1
        
    result = one + two
    while result != 0:
        answer += str(result%2)
        result = result // 2
            
    return answer[::-1]