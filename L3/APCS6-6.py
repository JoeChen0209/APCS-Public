# start
import sys
# 預設學生人數
students = [4, 3, 2, 1]
# 1計算總人數
# 2加入一個學生至串列尾端(append)
# 3從串列中移除一個學生(remove)
# 4排序學生的號碼(sort)

for s in sys.stdin:
    command = s.split()
    if len(command) == 1:
        # 判斷 1,4只有一個數字的指令
        if command[0] == "1":
            print(len(students))
        elif command[0] == "4":
            students.sort()
            print(students)
    elif len(command) == 2:
        # 判斷2,3含有兩個數字的指令
        if command[0] == "2":
            students.append(int(command[1]))
            print(students)
        elif command[0] == "3":
            students.remove(int(command[1]))
            print(students)
