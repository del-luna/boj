def dfs(x, y, k, prob, visited):
    global ans
    if k == n:
        if len(set(visited)) == n+1:
            ans += prob
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y+dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, k+1, prob*p[i], visited)
            visited.pop()

n, east, west, south, north = map(int, input().split())
p = [east/100, west/100, south/100, north/100]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

dfs(0,0,0,1,[(0,0)])
print(f'{ans:.10f}')