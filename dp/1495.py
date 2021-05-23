'''
n : 곡 개수
s : 시작 볼륨
m : 최대 볼륨
array : 각 곡의 시작전에 줄 수 있는 볼륨 차이
'''

n,s,m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j + volumes[i-1] <= m:
            dp[i][j + volumes[i-1]] = 1
        if j - volumes[i-1] >= 0:
            dp[i][j - volumes[i-1]] = 1
            
for idx, v in enumerate(reversed(dp[-1])):
    if v==1:
        print(m-idx)
        break
    if idx == len(dp[n])-1:
        print(-1)
        break