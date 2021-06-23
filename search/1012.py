import sys 
sys.setrecursionlimit(10000)

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0 <= ny < m and s[nx][ny]==1:
            s[nx][ny]=0
            bfs(nx,ny)

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    s = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        b,a = map(int,input().split())
        s[a][b] = 1
    
    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                bfs(i,j)
                cnt +=1
    
    print(cnt)