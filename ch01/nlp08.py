def cipher(text):
    message = ""
    for ch in text:
        if ch.islower():
            message += chr(219-ord(ch))
        else:
            message += ch
    return message


print(cipher("I am Yuki Taya. Hello!"))
print(cipher("I zn Yfpr Tzbz. Hvool!"))

"""
==219から引いている理由==
文字：文字コード
a  ：97
z  ：122
97 + 122 = 219
よって 219 から引き算することで a~z は別の小文字に変換される.
また、復号も同時にできる.
 a ->  z  -> a
97 -> 122 -> 97
"""