def solution(my_string):
    answer = [0] * 52
    lan1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
        
    for i in range(len(my_string)):
        for j in range(len(lan1)):
            if my_string[i] == lan1[j]:
                answer[j] += 1
                #print(i, j)

    return answer