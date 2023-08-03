s = input()
data = s.split()
temp = int(data[0])
weather = data[1]
print("今天的氣溫是%d度,天氣是%s天" % (temp, weather))
print("今天的氣溫是{}度,天氣是{}天".format(temp, weather))
print(f'今天的氣溫是{temp}度,天氣是{weather}天')
