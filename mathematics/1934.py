def gcd(a, b):
    return gcd(b, a%b) if b else a
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    ans = gcd(x, y)
    print(int(ans*(x/ans)*(y/ans)))