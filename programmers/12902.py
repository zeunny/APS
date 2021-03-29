def solution(n):
    if n % 2: 
        return 0
    
    dp = [0,3,11]
    index = n//2
    
    if index < 3: 
        return dp[index]

    for i in range(3, index+1):
        dp.append((dp[i-1]*3+sum(dp[1:i-1])*2+2)%1000000007)

    return dp[index]