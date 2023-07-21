# start

for i in range(4):
    for j in range(5):
        print("*", end="")
    print("")

print("================================================================")

for i in range(5+1):
    print("*"*i)

print("================================================================")

for i in range(5):
    print(" "*(4-i)+"*"*(i+1))
