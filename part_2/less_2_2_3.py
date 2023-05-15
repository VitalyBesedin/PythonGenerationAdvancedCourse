# put your python code here
numbers = [int(num) for num in input().split()]
bersnum = list()
for i in range(1, len(numbers), 2):
    bersnum.append(numbers[i])
    bersnum.append(numbers[i - 1])
if len(numbers) % 2 == 1:
    bersnum.append(numbers[-1])

print(*bersnum)
