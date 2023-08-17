import random
N = int(input())
N_list = []

for i in range(N):
    N_list.append(random.randint(1, 100))
print(N_list)
# 內建函式
# max_value = max(N_list)
# min_value = min(N_list)
max_value = 0
min_value = 100000000000000
# 線性搜尋
for i in range(len(N_list)):
    if N_list[i] > max_value:
        max_value = N_list[i]
    if N_list[i] < min_value:
        min_value = N_list[i]


print(max_value)
print(min_value)
