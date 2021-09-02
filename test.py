import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,cnt):
    
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x+int(graph[x][y])*dx[i]
        ny = y+int(graph[x][y])*dy[i]

        if 0<= nx < n and 0 <= ny < m and graph[nx][ny] != 'H' and cnt+1>dp[nx][ny]:
            if visited[nx][ny]: # cycle
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx,ny,cnt+1)
                visited[nx][ny] = False


dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = 0
dfs(0,0,0)

print(ans+1)