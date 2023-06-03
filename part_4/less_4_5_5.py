# Diagonal exchange
n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]


for i in range(n):
    matrix[i][i], matrix[-i - 1][i] = matrix[-i - 1][i], matrix[i][i]


for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
