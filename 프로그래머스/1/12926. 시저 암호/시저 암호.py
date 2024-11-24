def solution(s, n):
    big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] * 2
    small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] * 2
    answer = []
    li = list(map(str, s))
    
    for i in range(len(li)):
        if li[i].isupper():
            for j in range(len(big)//2):
                if big[j] == li[i]: 
                    answer.append(big[j+n])
        elif li[i] == " ":
            answer.append(" ")
        else:
            for j in range(len(small)//2):
                if small[j] == li[i]:
                    answer.append(small[j+n])
    return "".join(answer)