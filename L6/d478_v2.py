nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
if 1 <= n and n <= 100 and 1 <= m and m <= 10000:
    for i in range(n):
        count = 0
        data1 = list(map(int, input("").split()))
        data2 = list(map(int, input("").split()))
        data = data1+data2
        data.sort()
        for j in range(len(data)-1):
            if data[j] == data[j+1]:
                count += 1
        print(count)
