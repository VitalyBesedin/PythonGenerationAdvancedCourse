# put your python code here
numbers = [int(input()) for _ in range(int(input()))]
mults = [numbers[i] * numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i != j]
mult = int(input())
if mult in mults:
    print('ДА')
else:
    print('НЕТ')
