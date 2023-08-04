import sys


def temp(c):
    f = c*(9/5)+32
    return f


# start
for s in sys.stdin:
    c = int(s)
    f = temp(c)
    print(f)
