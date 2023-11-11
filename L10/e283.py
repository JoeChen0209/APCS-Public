# https://zerojudge.tw/ShowThread?postid=32070&reply=0
import sys
dic = {"0 1 0 1": "A",
       "0 1 1 1": "B",
       "0 0 1 0": "C",
       "1 1 0 1": "D",
       "1 0 0 0": "E",
       "1 1 0 0": "F"
       }

for i in sys.stdin:
    n = int(i)
    output = ""
    for j in range(n):
        data = sys.stdin.readline().strip()
        output += dic[data]
    print(output)
