def dfs(x):
    #x: current state
    global cnt

    if sum(graph[x])==0:
        return

    for i, k in enumerate(graph[x]):
        if k == 1:
            cnt+=1
            dfs(i)

    return cnt


n, m = map(int, input().split())
answers = {}

graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b-1][a-1] = 1

for i in range(n):
    cnt = 0
    answers[i+1] = dfs(i)

print(answers)