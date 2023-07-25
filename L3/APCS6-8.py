import sys
# start
peoples = {"A": 0, "B": 0, "C": 0}

for s in sys.stdin:
    s = int(s)  # 不能直接使用文字型態判斷是因為s文字型態時會包含\n
    if s == 1:
        peoples["A"] = peoples["A"]+1  # 不能直接使用+=
    elif s == 2:
        peoples["B"] = peoples["B"]+1
    elif s == 3:
        peoples["C"] = peoples["C"]+1
    print(peoples)
