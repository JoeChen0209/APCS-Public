a = 0
b = 0
z = False
result = 0
Data = input()
Data = Data.split(" ")
D = list(map(int, Data))
a = D[0]
b = D[1]
print(type(a))
print(type(b))
result = D[2]
print(type(result))
print(a and b)
print(result)
if a or b == result:
    print("OR")
    z = True
if str(a and b) == str(result):
    print("AND")
    z = True
if abs(a-b) == 1:
    print("XOR")
    z = True
if z == False:
    print("IMPOSSIBLE")
