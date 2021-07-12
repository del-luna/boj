def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in range(1, N+1):
        if visited[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    queue = [start]
    visited[start] = 0
    while queue:
        start = queue[0]
        print(start, end=' ')
        del queue[0]
        for i in range(1, N+1):
            if visited[i] == 1 and graph[start][i] == 1:
                queue.append(i)
                visited[i] = 0
            
            
N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
bfs(V)