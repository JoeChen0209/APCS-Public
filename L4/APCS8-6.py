# 引入數學模組
import math

# 設定PI值
PI = math.pi
# 輸入圓半徑
r = float(input(""))
# 計算圓周長
circumference = 2*r*PI
# 計算圓面積
area = r*r*PI

# 輸出
print(round(circumference, 2))
print(round(area, 2))
