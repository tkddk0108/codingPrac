def solution(my_string, m, c):
    answer = ''
    string = ''
    li = []
    for i in range(len(my_string)//m):
        li.append(my_string[:m])
        my_string = my_string[m:]
    print(li)
    
    for i in range(len(li)):
        string = str(li[i])
        answer += string[c-1]

    return answer