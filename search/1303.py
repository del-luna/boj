from collections import deque

def bfs(x, y, color):
    cnt = 0
    queue = deque()
    queue.append((x,y))
    graph[x][y] == 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] == color:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return 1 if cnt==0 else cnt

M, N = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
w,b=0,0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if graph[i][j] !=0 :#already visit
            if graph[i][j] == 'W':
                w += bfs(i,j,graph[i][j])**2
            else:
                b += bfs(i,j,graph[i][j])**2

print(w,b)