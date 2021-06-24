N = int(input())
n = int(input())
graph = dict()
visited = []

def bfs(start, graph):
    queue = [start]
    while queue:
        for i in graph[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

for i in range(1, N+1):
    graph[i] = []

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1, graph)
print(len(visited)-1)