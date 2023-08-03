from datetime import date
import sys

# start
time = []

for s in sys.stdin:
    data = list(map(int, s.split(" ")))
    time.append(data)
    # 抓到兩組時間就不繼續儲存
    if len(time) == 2:
        break
time1 = date(time[0][0], time[0][1], time[0][2])
time2 = date(time[1][0], time[1][1], time[1][2])
days = abs(time2-time1)
print(days)
