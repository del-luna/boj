w = int(input())
word_list = [''.join(input().strip()) for _ in range(w)]
print(word_list)

b = int(input())
boggle_list = []

for _ in range(b):
    boggle_list.append([])
    for _ in range(4):
        boggle_list[b].append(list(input().strip()))

print(boggle_list)