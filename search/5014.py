from collections import deque

def bfs(h):
    q = deque()
    q.append(h)
    visited = [0 for _ in range(f)]
    visited[h] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + step[i]
            if 0 <= nx < f and visited[nx] == 0: # Move within range & not visited
                q.append(nx)
                height[nx]=height[x] + 1
                visited[nx] = 1

f,s,g,u,d = map(int, input().split())
height = [-1 for _ in range(f)]
step = [u, -d]
height[s-1] = 0 #first floor
bfs(s-1)
print(height[g-1] if height[g-1] != -1 else "use the stairs")