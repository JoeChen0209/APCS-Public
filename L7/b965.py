# 取得第一個矩陣及指定操作內容
Data1 = input().split(" ")
R1 = int(Data1[0])  # 接下來有 R 行(line)是 矩陣B 的 內容
C1 = int(Data1[1])  # 每一行(line)都包含 C 個正整數
M1 = int(Data1[2])  # 在矩陣內容後的一行有 M 個整數，表示對 矩陣A 進行的操作。
matrix_list1 = []  # 儲存矩陣的二維陣列

# 先將陣列輸入為二維陣列
for i in range(R1):
    list_temp = input().split(" ")
    matrix_list1.append(list_temp)
# 再將操作紀錄下來
job1 = input().split(" ")


# 取得第二個矩陣及指定操作內容
Data2 = input().split(" ")
R2 = int(Data2[0])  # 接下來有 R 行(line)是 矩陣B 的 內容
C2 = int(Data2[1])  # 每一行(line)都包含 C 個正整數
M2 = int(Data2[2])  # 在矩陣內容後的一行有 M 個整數，表示對 矩陣A 進行的操作。
matrix_list2 = []  # 儲存矩陣的二維陣列

# 先將陣列輸入為二維陣列
for i in range(R2):
    list_temp = input().split(" ")
    matrix_list2.append(list_temp)
# 再將操作紀錄下來
job2 = input().split(" ")

print("R1/C1/M1=", R1, "/", C1, "/", M1)
print(matrix_list1)
print(job1)
print("R2/C2/M2=", R2, "/", C2, "/", M2)
print(matrix_list2)
print(job2)
