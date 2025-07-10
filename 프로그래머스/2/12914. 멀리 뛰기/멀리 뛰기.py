def solution(n):
    answer = 0
    if n == 1:return 1
    if n == 2:return 2
    dp = [1,2]
    for i in range(2,n):
        dp.append(dp[-1]+dp[-2])
    return dp[n-1]%1234567
    
        