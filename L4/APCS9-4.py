# ord(c)：將字元轉為 ASCII 值
# chr(value)：將數值轉為 ASCII 對應的文字
import sys
Lucky_dic = {0: "Lucky Ball", 1: "Lucky Sheep",
             2: "Lucky Guy", 3: "OK", 4: "Good Luck"}

for s in sys.stdin:
    words = s
    count = 0  # while迴圈記數用
    even_sum = 0  # 偶數ASCII值加總用
    odd_sum = 0  # 奇數ASCII值加總用

    while count < len(words):
        if count % 2 == 0:
            even_sum += ord(words[count])
        elif count % 2 != 0:
            odd_sum += ord(words[count])
        count += 1

    ans = Lucky_dic[(abs(even_sum-odd_sum)) % 5]
    print(ans)
