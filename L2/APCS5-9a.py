# start

# 設定前四行
for i in range(4, 0, -1):
    # 分為左+中+右
    print(" "*(i)+"* "*(5-i)+" "*(i-1))

# 設定中間那行(要移除最右邊多餘的空格)
str1 = "* "*5
print(str1.rstrip())

# 設定後四行
for i in range(1, 5, 1):
    # 分為左+中+右
    print(" "*(i)+"* "*(5-i)+" "*(i-1))
