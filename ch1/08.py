# 08_暗号文


# 与えられた文字列の各文字を以下の仕様で変換する関数
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
def cipher(Input):
    ans = ""
    for i in range(len(Input)):
        if 'a' <= Input[i] and Input[i] <= 'z':
            ans += chr(219 - ord(Input[i]))
        else:
            ans += Input[i]
    return ans


S = "I am Haruka."
print("暗号化: \"" + S + "\" -> \"" + cipher(S) + "\"")
S2 = cipher(S)
print("復号化: \"" + S2 + "\" -> \"" + cipher(S2) + "\"")
