import sys
# start

for s in sys.stdin:
    score = int(s)
    if score >= 80:
        print("A")
    elif score >= 60 and score < 80:
        print("B")
    else:
        print("C")
