# filling by snake
n, m = [int(i) for i in input().split()]
matrix = [[ i * m + j + 1 for j in range(m)] for i in range(n)]

for i in range(1,n,2):
    matrix[i].reverse()


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

