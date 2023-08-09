def push(data):
    # 放入資料
    stack.append(data)


def pop():
    # 取出資料
    ans = stack.pop()
    return ans


def top(data):
    # 取出最後放入的資料
    size = len(data)
    t = stack[size-1]
    return t


def size():
    size = len(stack)
    return size


def empty():
    if len(stack) == 0:
        return True
    else:
        return False


stack = [1, 2, 3, 4, 5]

print("在最尾部加入資料")
push(6)
print("取出最後放入資料")
print(pop())
print("取出所有資料中的最後(頂)一項")
print(top(stack))
print("取得目前stack串列中的元素數量")
print(size())
print("確認stack陣列是否沒有元素存在")
print(empty())
