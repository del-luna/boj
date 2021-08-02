def bfs(x, y):
    queue = [[x, y]]
    graph[x][y] = '0'
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1':
                graph[nx][ny]='0'
                queue.append([nx, ny])
                count+=1
    cnt.append(count)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = []
N = int(input())
graph = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            bfs(i, j)

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)