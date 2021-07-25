'''
#floyd warshall
import sys

INF = sys.maxsize
n, m = map(int, input().split())
a = [[INF]*n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    a[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 0
            else:
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])

ans = []
for i in a:
    ans.append(sum(i))
for i in range(n):
    if ans[i] == min(ans):
        print(i+1)
        break

'''



from collections import deque

def bfs(x):
    q.append(x)
    c = [-1 for _ in range(n)]
    c[x] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if c[i] == -1:
                c[i] = c[x] + 1
                q.append(i)
    cnt = 0
    for i in range(n):
        if c[i] != -1:
            cnt += c[i]
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
q, res, ans = deque(), [], []

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    res.append(bfs(i))

for i in range(n):
    if res[i] == min(res):
        ans.append(i)

print(min(ans)+1)