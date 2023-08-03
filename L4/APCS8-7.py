import random

count = int(input())
dice = []
for i in range(count):
    dice.append(random.randint(1, 6))

# 輸出各骰子點數
for i in range(count):
    print(dice[i], end=" ")
print()  # 換行

# 輸出點數加總
sum = sum(dice)
print(sum)
