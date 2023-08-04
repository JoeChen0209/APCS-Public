import sys


def add(a, b):
    c = a+b
    return c


def sub(a, b):
    c = a-b
    return c


def mul(a, b):
    c = a*b
    return c


def div(a, b):
    c = a/b
    return c


# start
for s in sys.stdin:
    data = s.split()
    num1 = int(data[0])
    calculator = data[1]
    num2 = int(data[2])
    if calculator == "+":
        print(add(num1, num2))
    elif calculator == "-":
        print(sub(num1, num2))
    elif calculator == "*":
        print(mul(num1, num2))
    elif calculator == "/":
        if num2 == 0:
            print("N/A")
            continue
        else:
            print(div(num1, num2))
