import sys
from collections import deque


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

n = int(input())
graph = [list(input())for _ in range(n)] 
f = [list(map(int, input().split())) for _ in range(n)]
houses = 0
fatigue = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'P':
           sx, sy = i, j
        if graph[i][j] == 'K':
            houses += 1

        fatigue.append(f[i][j])

fatigue = sorted(set(fatigue))
left, right = 0, 0
ans = sys.maxsize

while left < len(fatigue):
    visit = [[False] * n for _ in range(n)]
    init_tired = f[sx][sy]

    q = deque()
    K = 0 # num of visited home
    if fatigue[left] <= init_tired <= fatigue[right]:
        visit[sx][sy] = True
        q.append((sx,sy))
    
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] : continue
                init_tired = f[nx][ny]
                if fatigue[left]<= init_tired <= fatigue[right]:
                    visit[nx][ny] = True
                    q.append((nx,ny))
                    if graph[nx][ny] == 'K': K+=1
    
    if K == houses:
        ans = min(ans, fatigue[right] - fatigue[left])
        left+=1
    elif right + 1< len(fatigue):
        right += 1
    else: break

print(ans)