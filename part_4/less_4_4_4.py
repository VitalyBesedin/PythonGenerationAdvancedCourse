# put your python code here
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] > sum(matrix[i])/len(matrix[i]):
            count +=1
    print(count)
