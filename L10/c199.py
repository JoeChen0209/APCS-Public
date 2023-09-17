from webbrowser import get
data = list(map(int, input("").split()))
count = 0
# 移除連續重複項
c = 0
while True:
    if data[c] == data[c+1]:
        del data[c]
    elif data[c] != data[c+1]:
        c += 1
    if c == len(data)-1:
        break


# 找出當中最高的山頭有幾座即可
# 第一個與最後一個高度不考慮其為小山頭
# 但還是需要第一個與最後一個來做計算
for i in range(1, len(data)-1, 1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        count += 1
# print("data:", data)
# print("highest:", highest)
# print("count:", count)
print(count)
