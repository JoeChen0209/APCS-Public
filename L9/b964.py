students = int(input(""))
score = list(map(int, input("").split(" ")))
score.sort()

high = -1
low = 101
for i in range(len(score)):
    # 先算及格裡面最低的
    if score[i] >= 60 and score[i] <= low:
        low = score[i]
        # 再算不及格裡面最高的
    elif score[i] < 60 and score[i] >= high:
        high = score[i]

for i in score:
    print(str(i)+" ", end="")
print("")
if high == -1:
    print("best case")
else:
    print(high)

if low == 101:
    print("worst case")
else:
    print(low)
