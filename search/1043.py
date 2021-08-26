n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])

party_list = []
possible_list = []


for _ in range(m):
    party_list.append(set(list(map(int, input().split()))[1:]))
    possible_list.append(1)

for _ in range(m):
    for i, party in enumerate(party_list):
        if truth.intersection(party):
            possible_list[i] = 0
            truth = truth.union(party)

print(sum(possible_list))