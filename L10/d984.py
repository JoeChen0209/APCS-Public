import sys
for s in sys.stdin:
    dic = {0: "A", 1: "B", 2: "C"}
    data = list(map(int, s.split()))
    Max = max(data)
    iMax = data.index(Max)
    data[iMax] = 0
    if Max > sum(data):
        print(dic[iMax])
    else:
        print(dic[data.index(max(data))])
