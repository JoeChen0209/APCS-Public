def CheckUpperChar(checklist, k):
    for i in range(k):  # 檢查連續k個數是否皆為大寫
        if checklist[i].islower():
            return False  # 只要有一個是小寫就回傳Fasle
    return True    # 都是就回傳True


def CheckLowerChar(cheklist, k):
    for i in range(k):    # 檢查連續k個數是否皆為小寫
        if cheklist[i].isupper():
            return False    # 一個是大寫就回傳False
    return True    # 都是就回傳True


k = int(input(""))
data_input = input("")
data = []
for i in data_input:
    data.append(i)
bestscore = 0
for i in range(len(data)-k+1):  # 從頭開始每K個送出去做一次檢查
    char_status = "upper"  # 檢查這次出去的status為大寫or小寫
    if data[i].islower() == True:
        char_status = "lower"
    elif data[i].isupper() == True:
        char_status = 'upper'
    j = i
    score = 0
    while j < len(data)-k+1:
        checklist = []
        result = False
        for x in range(j, j+k, 1):
            checklist.append(data[x])
        j += k
        if char_status == "upper":  # 送出去檢查接下來的連續K個是否都為大寫
            result = CheckUpperChar(checklist, k)
            if result == True:
                score += k
                if score > bestscore:
                    bestscore = score    # 取代最高紀錄
                char_status = "lower"
            elif result == False:
                score = 0
                break
        elif char_status == "lower":  # 送出去檢查接下來的連續K個是否都為小寫
            result = CheckLowerChar(checklist, k)
            if result == True:
                score += k
                if score > bestscore:
                    bestscore = score  # 取代最高紀錄
                char_status = "upper"
            elif result == False:
                score = 0
                break
print(bestscore)
