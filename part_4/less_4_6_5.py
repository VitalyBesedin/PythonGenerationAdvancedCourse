n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    matrix[i][i], matrix[-i - 1][i] = 1, 1


for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()

