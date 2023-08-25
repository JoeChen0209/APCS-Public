# 身分證字號檢查
import sys
for s in sys.stdin:
    first_char = s[0]
    print(first_char.isnumeric())
    data = []
    for i in s:
        print(i)
        data.append(i)
    del data[-1]
    print(data)
