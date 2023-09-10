#C295

# 題目
# 有N群
# 每群都有M個整數
# S=從每群中選出最大的數字加總起來
# 在所有最大數裡面找出可以整除S的print出來

# Input
mn=input()
data=[]
mn_list=list(map(int,mn.split()))
m=mn_list[0]
n=mn_list[1]
for i in range(m):#輸入幾行
    data.append(list(map(int,input().split())))

# Process
#找出各集合的最大數並加總起來
max_data=[]
s=0
for i in range(len(data)):
    max_data.append(max(data[i]))
s=sum(max_data)
print(s)

#S去除每次找到的數字檢查是否可以整除
num_list=""
for i in max_data:
    if s % i==0:
        num_list=num_list+str(i)+" "
if num_list=="":print("-1")
else:print(num_list.strip())