list = input().split()
n = int(input())
list_res = []

for i in range(0,len(list),n):
    list_res.append([list[i]])
    count = 1
    while n > count:
        if i + count < len(list):
            list_res[-1].append(list[i + count])
        count += 1

print(list_res)

