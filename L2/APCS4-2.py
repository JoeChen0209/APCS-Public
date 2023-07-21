import sys
# start

# 使用單次輸入取得及格成績
pass_score = int(input(""))

# 使用連續輸入取得需要檢查的成績
for s in sys.stdin:
    # 將每次輸入的文字型態成績轉為數字型態成績(可以在此加入檢查機制)
    test_score = int(s)
    # 判斷成績是否超過及格成績並print出對應的結果
    if test_score >= pass_score:
        print("pass")
    else:
        print("fail")
