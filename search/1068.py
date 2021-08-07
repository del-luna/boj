def dfs(root):
    global count
    isTrue = False
    visited[root] = 1
    for i in range(n):
        if graph[root][i] == 1 and visited[i] == 0:
            isTrue = True
            dfs(i)
    if isTrue == False:
        count += 1

n = int(input())
tree = list(map(int, input().split()))
d = int(input())
graph = [[0]*n for _ in range(n)]
visited = [0]*n
count = 0

for i in range(len(tree)):
    if tree[i] != -1:
        graph[i][tree[i]] = 1
        graph[tree[i]][i] = 1
    else:
        root = i

for i in range(n):
    graph[i][d] = 0
    graph[d][i] = 0

dfs(root)
if d == root:
    print(0)
else:
    print(count)