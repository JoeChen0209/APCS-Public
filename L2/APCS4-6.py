import sys
# start
for s in sys.stdin:
    year = int(s)
    if year % 4 != 0:
        print("No")
    elif year % 4 == 0 and year % 100 != 0:
        print("Yes")
    elif year % 100 == 0 and year % 400 != 0:
        print("No")
    elif year % 400 == 0:
        print("Yes")
