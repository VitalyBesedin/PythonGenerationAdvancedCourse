# First line numbers
myset1 = set([int(n) for n in input().split()])
myset2 = set([int(n) for n in input().split()])

print(*sorted(myset1 - myset2))
