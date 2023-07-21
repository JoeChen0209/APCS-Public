# start
# for迴圈寫法
num = int(input())
for i in range(1, num+1, 1):
    if num % i == 0:
        print(i, end=" ")

# while迴圈寫法
print("")
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
