import sys
# he---ll[o], wo?r#l^d!
no_need_to_keep = "()-[]}{;:<>?@#$%^&*"

for s in sys.stdin:
    words = list(s)
    ans = ""
    for word in words:
        # 每一個不在要消除的清單內的字就加入到ans裡面
        if word not in no_need_to_keep:
            ans += word
    print(ans)
