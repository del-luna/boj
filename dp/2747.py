def fib(n):
    if n==0 or n==1:
        return 1
    dp = [0, 1]
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

print(fib(int(input())))