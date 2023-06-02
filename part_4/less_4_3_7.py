# put your python code here
start_list = [_ for _ in input().split()]
final_list = [[]]
add_list = []
for i in range(len(start_list)):
    for j in range(len(start_list)):
        add_list = start_list[j:i+j+1]
        if len(add_list) == i + 1:
            final_list.append(add_list)


print(final_list)

