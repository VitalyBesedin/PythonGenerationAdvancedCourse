# change matrix's calls
n, m = int(input()), int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(n)]
list = input().split()
i , j = int(list[0]),int(list[1])
for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
