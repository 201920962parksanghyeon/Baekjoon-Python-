def N(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    su = N(m) // (N(n) * N(m - n))
    print(su)