# set three words
s1,s2,s3 = input().split()

if set(s1) == set(s2) == set(s3):
    print('YES')
else:
    print('NO')
