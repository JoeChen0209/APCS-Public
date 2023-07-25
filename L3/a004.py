#a004
import sys
for s in sys.stdin:
    year=int(s)
    if (year%4==0 and year%100!=0) or year%400==0:
        print("閏年")
    else:print("平年")