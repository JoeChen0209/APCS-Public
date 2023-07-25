# start

week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# print(week.index("Tue"))
date = int(input())
day = input()
start_day = week.index(day)
next_date = int(input())
# 計算日期，記得要加上起始日期
next_day = week[(next_date-date+start_day) % 7]
print(next_day)
