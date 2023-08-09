def enqueue(data):
    queue.appen(data)


def dequeue():
    data = queue.pop(0)
    return data


def isFull():
    if len(queue) == max_size:
        return True
    else:
        return False


def isEmpty():
    if len(queue) == 0:
        return True
    else:
        return False


def front():
    return queue[0]


def rear():
    return queue[len(queue)-1]


# start
queue = []
max_size = 10

# 連續加入 11 個資料進入 queue，如果超過 MAX_SIZE 就禁止進入
for i in range(11):
    if isFull() == False:
        enqueue(i)
    else:
        print("Queue is full, can not add any more data")

# 從 queue 中連續輸出資料，輸出前先檢查 queue 是否為空，如果空的就不能再輸出資料
for i in range(6):
    if isEmpty() == False:
        print(dequeue(), queue)
    else:
        print("Queue is empty, can not remove any more data")
