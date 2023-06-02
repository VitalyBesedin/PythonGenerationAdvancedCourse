n, m = int(input()), int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(n)]
max_matrix = matrix[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_matrix:
            max_i = i
            max_j = j
            max_matrix = matrix[i][j]
        else:
            continue

print(max_i, max_j)
