def cipher(str):
    ans = [chr(219 - ord(x)) if x.islower() else x for x in str]
    return ''.join(ans)

#例
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

sentence = cipher(sentence)
print("暗号化:",sentence)
sentence = cipher(sentence)
print("復号化:",sentence)