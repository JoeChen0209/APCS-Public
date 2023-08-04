# ord(c)：將字元轉為 ASCII 值
# chr(value)：將數值轉為 ASCII 對應的文字
import sys

for s in sys.stdin:
    data = s.split(" ")
    words = data[0]
    num = int(data[1])
    ans = ""
    for word in words:
        ans += chr(ord(word)+num)
    print(ans)
