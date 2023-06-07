# chess knight move
n = 8
matrix = [['.'] * n for _ in range(n)]  # ajhvbhetv vfnhbwe bp njxtr
cell = list(input())  # делаем из клетки список
call = list('abcdefgh')  # формируем индексы вертикалей
row = list('87654321')  # формируем индексы горизонталей
# определяем индексы клетки коня
x = row.index(cell[1])
y = call.index(cell[0])
matrix[x][y] = 'N'  # ставим коня на доску
for i in range(n):
    for j in range(n):
        if (x-i)**2 + (y-j)**2 == 5:
            matrix[i][j] = '*'

for r in range(n):  # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
