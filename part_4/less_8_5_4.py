# Has the number been seen before?
numbers = [int(c) for c in input().split()]

s = set()
for n in numbers:
    if n in s:
        print('YES')
    else:
        s.add(n)
        print('NO')

