import sys


def addvalue(a, b):
    c = int(a)+int(b)
    return c


def addstring(a, b):
    c = str(a)+str(b)
    return


for s in sys.stdin:
    data = list(map(int, s.split()))
    if data[0] == 1:
        print(addvalue(data[1], data[2]))
    elif data[0] == 2:
        print(addstring(data[1], data[2]))
