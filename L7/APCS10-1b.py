import sys

for s in sys.stdin:
    data = list(map(int, s.split()))
    N = data[0]
    del data[0]
    print(N)
    print(data)
