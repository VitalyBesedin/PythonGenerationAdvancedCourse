# put your python code here
quantity = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:',
         'Третья четверть:', 'Четвертая четверть:']

for i in range(quantity):
    x, y = [int(num) for num in input().split()]
    if x != 0 or y !=0:
        if x > 0 and y >0:
            count[0] += 1
        elif x > 0 and y < 0:
            count[3] += 1
        elif x < 0 and y < 0:
            count[2] += 1
        elif x < 0 and y > 0:
            count[1] += 1
for j in range(len(count)):
    print(names[j], count[j])
