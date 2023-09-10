#C461

output=[]
data=list(map(int,input().split()))
if data[0]!=0:a=1
else:a=data[0]
if data[1]!=0:b=1
else:b=data[1]
c=data[2]


#判斷and
if (a and b) == c:output.append("AND")
#判斷OR
if (a or b)== c:output.append("OR")
#判斷XOR(兩數相減為零)
if (abs(a-b))==c:output.append("XOR")
#都沒有就是IMPOSSIBLE
if len(output)==0:
    print("IMPOSSIBLE")
else:
    for o in output:
        print(o)
