# put your python code here
n = int(input())

my_list = [[i for i in range(1,n + 1)] for _ in range(n)]
print(*my_list, sep='\n')