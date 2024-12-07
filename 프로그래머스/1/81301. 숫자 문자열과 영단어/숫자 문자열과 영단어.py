def solution(s):
    answer = ''
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    word = ''
    for i in s:
        if i.isdigit():
            if word != '':  
                answer += str(num.get(word,''))
                word = ''
            answer += str(i)
        else:
            word += i
            if word in num:
                answer += str(num.get(word,''))
                word = ''
    return int(answer)