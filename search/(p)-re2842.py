from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x, y, left, right):
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if left <= h[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])

    for i, j in home:
        if not c[i][j]:
            return 0
    return 1

n = int(input())

a, home = [], []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if k == 'P' or k == 'K':
            home.append([i, j])

h, temp_set = [], set()
for i in range(n):
    row = list(map(int, input().split()))
    h.append(row)
    for k in row:
        temp_set.add(k)
temp_list = list(sorted(temp_set))
l_min = min(temp_list)
r_max = max(temp_list)

l_max, r_min = sys.maxsize, 0
for i, j in home:
    l_max = min(l_max, h[i][j])
    r_min = max(r_min, h[i][j])

lq, rq = [], []
for k in temp_list:
    if l_min <= k <= l_max:
        lq.append(k)
    if r_min <= k <= r_max:
        rq.append(k)

ans = sys.maxsize
i, j = 0, 0
while i < len(lq) and j < len(rq):
    l_flag, r_flag = 0, 0
    if bfs(home[0][0], home[0][1], lq[i], rq[j]):
        ans = min(ans, rq[j] - lq[i])
        i += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            i += 1; j += 1
        else:
            j += 1
            r_flag = 1
print(ans)