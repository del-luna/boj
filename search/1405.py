def dfs(x, y, k, prob, visited):
    global ans
    if k == n:
        pass
n, east, west, south, north = map(int, input().split())
p = [east/100, west/100, sout/100, nort/100]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0