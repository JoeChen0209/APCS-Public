import random

number = random.randint(1, 101)
count = 0
for i in range(100):
    if i == number:
        print("總共執行", count+1, "次")
        break
    else:
        count += 1
