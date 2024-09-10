def solution(my_string, queries):
    answer = ''
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        get = list(my_string[a:b+1])
        reverse = ''.join(reversed(get))
        my_string = my_string[:a]+reverse+my_string[b+1:]
    
    answer = my_string
    return answer