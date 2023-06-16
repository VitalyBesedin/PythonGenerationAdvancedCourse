# Filling with diagonals
n, m = [int(i) for i in input().split()]

lst = [[ 0 for j in range(m)] for i in range(n)]
nm = 0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                lst[i][j] = nm


for i in range(n):
    for j in range(m):
        print(str(lst[i][j]).ljust(3), end=' ')
    print()

