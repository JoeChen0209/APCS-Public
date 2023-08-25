# print("1=",ord("1"))
# print("*=",ord("*"))
data=input("")
data_list=[]

for i in data:
    data_list.append(i)
print(data_list)
for i in range(len(data_list)):
    print(chr(ord(data_list[i])-7),end="")