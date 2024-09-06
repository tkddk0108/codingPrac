def solution(code):
    answer = ''
    mode = 0
    iCount = 0
    ret = ''

    # 이 부분에서 TypeError: 'str' object cannot be interpreted as an integer 가 발생했다
    # 왜 그런가! 내가 'for j in code' 와 같이 j가 문자열의 문자 자체인 경우인데 숫자로 다루려고 했기 때문
    # 이를 해결하기 위해서는 j는 문자열에서 인덱스를 참조하고 code[j]와 같은 방식으로 문자를 다루어야 함
    
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
