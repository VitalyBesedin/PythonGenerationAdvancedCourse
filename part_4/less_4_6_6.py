n = int(input())

res = [[0 if i > j and i < n - 1 - j or i < j and i > n - 1 -j else 1 for j in range(n)] for i in range(n)]

for x in res:
    print(*x)
