n = int(input())
m = int(input())
friend = dict()

for i in range(1, n+1):
    friend[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

answer = set(friend[1])
for i in friend[1]:
    answer.update(friend[i])
print(len(answer) - 1)