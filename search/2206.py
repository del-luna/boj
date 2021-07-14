from collections import deque

def bfs():
    queue = deque()
    queue.append([0,0,1])
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visit [0][0][1] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y == M-1:
            return visit[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z == 1: # current state = wall and can break through
                    visit[nx][ny][0] = visit[x][y][1] + 1 
                    queue.append([nx, ny, 0])

                elif graph[nx][ny] == 0 and visit[nx][ny][z] == 0: #no visit and current state = no wall
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append([nx, ny, z])

    return -1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]

print(bfs())