def solution(nums):
    answer = 0
    n = len(nums)/2
    setnum = set(nums)
    if len(setnum) >= n:
        answer = n
    else:
        answer = len(setnum)
    return answer