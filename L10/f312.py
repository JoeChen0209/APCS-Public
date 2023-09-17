# 最大收益紀錄
record = []

# 輸入資料
data1 = list(map(int, input("").split()))
data2 = list(map(int, input("").split()))
# 工廠一收益參數
a1 = data1[0]
b1 = data1[1]
c1 = data1[2]
# 工廠二收益參數
a2 = data2[0]
b2 = data2[1]
c2 = data2[2]

# 員工總數
n = int(input(""))


# 工廠的收益

for i in range(n+1):
    # 工廠一/工廠二員工數
    x1 = i
    x2 = n-x1
    y1 = (a1*(x1**2))+(b1*x1)+c1
    y2 = (a2*(x2**2))+(b2*x2)+c2
    record.append(y1+y2)

print(max(record))
