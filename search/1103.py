from collections import deque

def dfs(x, y):
    global state
    if not(0<=x<n and 0<=y<m) or graph[x][y] == 'H':#game over
        return 0
    if visited[x][y]: #cycle
        state = True
        return -1
    if memo[x][y] != -1:
        return memo[x][y]

    visited[x][y] = True #current = True
    for k in range(4):
        memo[x][y] = max(memo[x][y], dfs(x + dx[k]*int(graph[x][y]), y + dy[k]*int(graph[x][y])) + 1)
        if state:
            return -1
    visited[x][y] = False

    return memo[x][y]

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
memo = [[-1]*m for _ in range(n)]
state = False
print(dfs(0, 0))