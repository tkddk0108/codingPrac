def solution(s):
    answer = -1
    stack = []
    for i in range(len(s)):
        if stack != [] and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

            
    if stack== []: return 1
    else: return 0

    return answer