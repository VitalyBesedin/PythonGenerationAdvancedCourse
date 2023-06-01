# put your python code here
n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]

max = matrix[0][0]

for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] > max:
            max = matrix[i][j]
print(max)
