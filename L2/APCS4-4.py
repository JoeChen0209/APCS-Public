import sys

# start

for s in sys.stdin:

    # 一共有三個數字並在同一行，使用split()方法切開，切開的依據為空格
    triangles = s.split(" ")

    # 將triangles串列(陣列)中的文字取出並強制轉換為整數型態方便計算
    a = int(triangles[0])
    b = int(triangles[1])
    c = int(triangles[2])

    # 計算任意兩邊相加是否皆>第三邊
    if a+b > c and a+c > b and b+c > a:
        print("Yes")
    else:
        print("No")
