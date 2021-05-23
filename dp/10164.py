n,m,k = map(int, input().split())
dp = [[1]*m for _ in range(n)]
tx = (k-1)//m
ty = m-1 if k%m == 0 else k%m-1 

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
if k==0:
    print(dp[n-1][m-1])
else:
    print(dp[tx][ty]*dp[n-tx-1][m-ty-1])