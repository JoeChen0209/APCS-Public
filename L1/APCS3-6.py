import sys

#start
for s in sys.stdin:
    date = s.split()
    number = (int(date[0])+int(date[1]))%10
    print(number)
    
