# 在堆疊頂端加入元素。
# 輸出堆疊最頂端的元素。
# 刪除堆疊最頂端的元素。
stack = []
# N = int(input("請輸入執行次數:"))
N = int(input(""))
for i in range(N):
    # k = int(input(""))
    data_str = input("")
    data_int = []
    if len(data_str) > 1:
        data_int = list(map(int, data_str.split()))
    else:
        data_int = list(map(int, data_str))
    k = data_int[0]

    if k == 1:
        # 請再讀入一個整數 x(1≤x≤10**9) ，並在堆疊頂端加入該整數。
        x = data_int[1]
        if x >= 1 and x <= 10**9:
            stack.append(x)
    elif k == 2:
        # 請輸出堆疊最頂端的元素，
        # 如果當前堆疊內沒有元素，請輸出 −1 。
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print("-1")
    elif k == 3:
        # 請刪除堆疊最頂端的元素，
        # 如果當前堆疊內沒有元素，請無視該操作
        if len(stack) != 0:
            stack.pop()
    # print(stack) #檢查用
