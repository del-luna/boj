def fib(n):
    if len(one) <= n:
        for i in range(len(one), n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(f"{zero[n]} {one[n]}")

if __name__ == "__main__":
  
    zero = [1, 0]
    one = [0, 1]

    t = int(input())
    for _ in range(t):
        fib(int(input()))