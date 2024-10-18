def solution(num, k):
    answer = 0
    num = str(num)
    if str(k) in num : return num.index(str(k))+1
    else: return -1
