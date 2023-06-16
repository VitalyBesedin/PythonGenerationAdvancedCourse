# filling 1
list  = input().split()
n, m = int(list[0]), int(list[1])
matrix = [[ i * m + j + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

