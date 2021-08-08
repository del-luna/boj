from collections import deque

def make_graph(edges):
    graph = {n + 1: [] for n in range(n)}

    for frm, to, cost in edges:
        graph[frm].append([to, cost])
        graph[to].append([frm, cost])

    return graph

def bfs(s, g):
    q = deque()
    visited = [0]*(n+1)
    q.append((s, 0))
    visited[s] = 1

    while q:
        cur, cost = q.popleft()
        if cur == g:
            return cost
        for next_state, d in graph[cur]:
            if not visited[next_state]:
                visited[next_state] = 1
                q.append((next_state, cost+d))


n, m = map(int, input().split())
tree = [list(map(int, input().split()))for _ in range(n-1)]
inputs = [list(map(int, input().split())) for _ in range(m)]
graph = make_graph(tree)

for x, y in inputs:
    answer = bfs(x, y)
    print(answer)