# 村民、狼人、攻擊範圍
data1 = list(map(int, input().split()))
people = data1[0]
wolf = data1[1]
attack = data1[2]

# 住家的距離list
data2 = list(map(int, input().split()))

# 計算狼的攻擊範圍是否涵蓋村民

# 如果村民在左邊，狼在右邊
if people < wolf:
    if sum(data2[people:wolf]) > attack:
        print("No")
    elif sum(data2[people:wolf]) <= attack:
        print("Yes")
else:
    # 如果村民在右邊，狼在左邊
    if sum(data2[wolf:people]) > attack:
        print("No")
    elif sum(data2[wolf:people]) <= attack:
        print("Yes")
