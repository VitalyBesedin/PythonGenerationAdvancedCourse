# put your python code here
n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if matrix[i][j] > largest and i >= j and i <= n - 1 - j:
            largest = matrix[i][j]
        elif matrix[i][j] > largest and i <= j and i >= n - 1 - j:
            largest = matrix[i][j]
        else:
            continue

print(largest)
