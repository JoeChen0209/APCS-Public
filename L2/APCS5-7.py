# start

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        if i*j < 10:
            print(str(i)+"x"+str(j)+"= "+str(i*j), end=" ")
        else:
            print(str(i)+"x"+str(j)+"="+str(i*j), end=" ")
    print("")
