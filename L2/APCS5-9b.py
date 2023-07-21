# start
strall = ""
for i in range(1, 6, 1):
    temp = ""
    if i % 2 != 0:
        temp = "0"+"10"*(i//2)
    else:
        temp = "10"*(i//2)
    print(temp)
# output
# 0
# 10
# 010
# 1010
# 01010
