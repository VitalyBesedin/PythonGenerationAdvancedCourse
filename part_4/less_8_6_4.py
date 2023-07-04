# General figures
n = int(input())
myset1 = set(input())
for _ in range(1,n):
    myset2 = set(input())
    myset1.intersection_update(myset2)

print(*sorted(myset1))
