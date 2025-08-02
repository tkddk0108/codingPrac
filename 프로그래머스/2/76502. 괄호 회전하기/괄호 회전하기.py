def check(s):
    stack = []
    pair = {']':'[', '}':'{', ')':'('}
    for char in s:
        if char in "{([":
            stack.append(char)
        elif char in "]})":
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
            
    return len(stack) == 0
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:]+s[0]
    return answer