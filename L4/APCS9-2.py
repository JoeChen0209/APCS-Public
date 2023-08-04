import sys

# 使用串列綜合表達式
for s in sys.stdin:
    num = [int(i) for i in s.split()]
    print(num)
# 使用字串映射轉換
for s in sys.stdin:
    num = list(map(int, s.split()))
    print(num)
