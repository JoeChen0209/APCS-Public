moneys = [50000, 30000, 120000]
# new_moneys = []

# 單獨取出設定
a = moneys[0]
b = moneys[1]
c = moneys[2]

a = a*1.01
b = b*1.01
c = c*1.01

moneys[0] = a
moneys[1] = b
moneys[2] = c


# 迴圈解決
# for i in range(len(moneys)):
#     moneys[i] *= 1.01

# 輸出結果
print(moneys)
