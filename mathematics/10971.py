from itertools import permutations

def search(per):
    tmp = 0
    for i in range(N - 1):
        if graph[per[i]][per[i+1]] != 0:
            tmp += graph[per[i]][per[i+1]]
        else:
            return False
    
    if graph[per[-1]][per[0]] == 0:
        return False
    else:
        tmp += graph[per[-1]][per[0]]
    
    return tmp

answer = 10000000000
N = int(input())
V = list(range(N))
graph = [list(map(int, input().split())) for _ in range(N)]

for p in permutations(V):
    tmp_ans = search(p)
    if tmp_ans:
        answer = min(tmp_ans, answer) 

print(answer)