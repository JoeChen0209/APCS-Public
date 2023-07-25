import sys
# start

for s in sys.stdin:
    # 依據空白分開數字
    num_list = s.split(' ')
    # 將文字型態轉為數字型態方便計算
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    # 輸出答案
    print(sum(num_list)/len(num_list))
