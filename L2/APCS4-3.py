import sys

# start
# 輸入數字
for s in sys.stdin:
    num = int(s)
    # 判斷奇數還是偶數
    if num % 2 == 0:
        # 偶數輸出even
        print("even")
    else:
        # 奇數輸出odd
        print("odd")
