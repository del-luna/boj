s, p = map(int, input().split())
prev = 0
k = 2
while 1:
    if s == p:
        print(1)
        break

    cur = pow(1.0 * s/k, k)
    if cur>= p:
        print(k)
        break

    elif cur < prev:
        print(prev)
        break
    prev = cur
    k+=1