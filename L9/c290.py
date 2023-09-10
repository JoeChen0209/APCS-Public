# abs() 函數返回數字的絕對值。

data = input("")
data_list = []
for i in data:
    data_list.append(int(i))
A = 0
B = 0
for i in range(len(data_list)):
    if i % 2 == 1:
        A += data_list[i]
    elif i % 2 == 0:
        B += data_list[i]

print(abs(A-B))
