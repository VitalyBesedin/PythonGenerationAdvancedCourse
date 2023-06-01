# put your python code here
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

tr = 0
for i in range(n):
    tr += matrix[i][i]
print(tr)
