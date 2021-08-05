n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right, count = 0, 0, 0

while left<=right and right<=n:
    part_sum = sum(a[left:right])

    if part_sum == m:
        count+=1
    if part_sum <= m:
        right+=1
        continue
    elif part_sum > m and left<right:
        left+=1
        continue
    else:
        left+=1
        right+=1
print(count)