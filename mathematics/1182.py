from itertools import combinations

n, s = map(int, input().split())
seq = list(map(int, input().split()))
cnt= 0

for i in range(1,n+1):
    cand = combinations(seq, i)
    for j in list(cand):
        if sum(j) == s:
            cnt += 1
print(cnt)