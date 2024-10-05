def solution(my_string):
    my_string = list(my_string)
    answer = my_string[::-1]
    string=''
    for i in answer:
        string += i
    return string