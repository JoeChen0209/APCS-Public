# start

import sys
for s in sys.stdin:
    data = list(map(int, s.split()))
    sum = 0
    for i in range(0, len(data)):
        sum += data[i]
    print(sum)
