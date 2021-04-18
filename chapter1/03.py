import re

sen = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

#センテンスを分ける
words = re.split(' ', sen)
words = [a.strip(",") for a in words]
words = [a.strip(".") for a in words]
print(words)

words_len = list(map(len, words))
print(words_len)




