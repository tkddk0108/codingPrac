def solution(code):
    answer = ''
    mode = 0
    iCount = 0
    ret = ''
    
    for j in range(len(code)):
        if mode == 0: 
            if j % 2 == 0 and code[j] != '1':
                ret += code[j]
            elif code[j] == '1':
                mode = 1
        else:
            if j % 2 == 1 and code[j] != '1':
                ret += code[j]
            elif code[j] == '1':
                mode = 0

    if ret == '':
        answer = "EMPTY"
    else:
        answer = ret
    
    return answer