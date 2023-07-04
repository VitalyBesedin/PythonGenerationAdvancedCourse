# All figures
set1 = set(input())
set2 = set(input())
if set1.issuperset(set2):
    print('YES')
else:
    print('NO')

# another version
# print(('NO', 'YES')[set(input()).issuperset(set(input()))])