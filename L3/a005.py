# a005
times=int(input())
for t in range(times):
    data=list(map(int,input().split()))
    if data[3]-data[2]==data[2]-data[1]:#等差數列
        data.append(data[3]+(data[3]-data[2]))
    else:data.append(int(data[3]*(data[3]/data[2])))
    for d in data:
        print(d,end=" ")
    print()