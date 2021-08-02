def bfs(x, y):
    queue = [[x, y]]
    max_f = 0
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]

        check = {}
        c = []
        for k in range(8):
            nx = a + dx[k]
            ny = b + dy[k]

            

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 'K':
                max_f = max(abs(f[a][b] - f[nx][ny]), max_f)
                print(max_f)
                graph[nx][ny] = -1
                queue.append([nx, ny])
                c = []
                check = {}
                break

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '.':
                c.append(graph[nx][ny])
                check[f[nx][ny]] = [nx, ny]

        if len(c)>0 and 'K' not in c:
            max_f = max(abs(f[a][b] - min(check)), max_f)
            print('error!')
            print(max_f)
            nx = check[min(check)][0]
            ny = check[min(check)][1]
            graph[nx][ny] = -1
            queue.append([nx, ny])
            check={}
            c=[]


    print(max_f)                


dx = [-1,0,1,-1,1,-1,0,1]
dy = [1,1,1,0,0,-1,-1,-1]

n = int(input())
graph = [list(input())for _ in range(n)] 
f = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'P':
           bfs(i, j) 