import random

# 初始化5個數字並使用random打亂
data = [int(x) for x in range(1, 6)]
random.shuffle(data)

count = 0
for i in range(0, len(data)):
    for j in range(0, len(data)-1-i):
        if data[j] > data[j+1]:
            # swap
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            count += 1
    print(data)
