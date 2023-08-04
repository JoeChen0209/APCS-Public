import math
# 資料輸入
position = input().split()
house = input().split()

# 文字型態轉換為整數型態方便後續計算
for i in range(len(position)):
    position[i] = int(position[i])
for i in range(len(house)):
    house[i] = int(house[i])

# 設定人的位置
people_position = position[0]
# 設定狼的位置
wolf_position = position[1]
# 設定狼的攻擊範圍
attack_range = position[2]

# 計算狼人與村民的距離(要區分左右)
if people_position < wolf_position:
    # 如果人在左邊狼在右邊，就從人的位置取到狼的位置
    distance = sum(house[people_position:wolf_position])
else:
    # 如果狼在左邊人在右邊，就從狼的位置取到人的位置
    distance = sum(house[wolf_position:people_position])

# 判斷是否狼人與村民的距離是否超出攻擊距離
if distance > attack_range:
    # 超出，不會被攻擊
    print("No")
else:
    # 沒超出，會被攻擊
    print("Yes")
