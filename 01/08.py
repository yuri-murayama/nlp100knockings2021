# 08_暗号文


# 与えられた文字列の各文字を以下の仕様で変換する関数
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
def cipher(str):
    ans = ""
    for i in range(len(str)):
        if 'a' <= str[i] and str[i] <= 'z':
            ans += chr(219 - ord(str[i]))
        else:
            ans += str[i]
    return ans


S = "I like Sushi."
print("暗号化: \"" + cipher(S) + "\"")
print("復号化: \"" + cipher(cipher(S)) + "\"")
