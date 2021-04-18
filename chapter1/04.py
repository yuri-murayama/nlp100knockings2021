import re
sen = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = re.split(' ', sen)
print(words)

#一文字目
initial = [1,5,6,7,8,9,15,16,19]

goal = {}

for i, word in enumerate(words):
    if i + 1 in initial:
        goal[i+1] = word[0]
    else:
        goal[i+1] = word[:2]

print(goal)

