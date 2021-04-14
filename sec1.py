
#00.文字列の逆順
l = "stressed"
l = l[::-1]
print("00: ",l)
print("\n")

#01. 「パタトクカシーー」
l = "パタトクカシーー"
l = l[::2]
print("01: ",l)
print("\n")

#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
a = "パトカー"
b = "タクシー"
l = ""
for i in range(len(a)):
    l = l + a[i] + b[i]
print("02: ",l)
print("\n")

#03. 円周率
l = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = l.split()
n = []
for i in range(len(l)):
    n.append(len(l[i].strip('.,')))
print("03: ",n)
print("\n")

#04. 元素記号
l = "Hi He Lied Because Boron Could Not Oxidize Fluorine.New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = l.split()
dic = {}

for i in range(len(l)):
    if i+1 in [1,5,6,7,8,9,15,16,19]:
        dic[i+1] = l[i][:1]
    else:
        dic[i+1] = l[i][:2]
print("04: ",dic)
print("\n")

#05. n-gram
import re
l = "I am an NLPer"
tango = l.split()
moji = l.replace(' ','')

bi_tango = []
for i in range(len(tango)-1):
    bi_tango.append(tango[i] + tango[i+1])

bi_moji =[]
for i in range(len(moji)-1):
    bi_moji.append(moji[i] + moji[i+1])

print("05 単語bi-gram: ",bi_tango)
print("05 文字bi-gram: ",bi_moji)
print("\n")

#06. 集合
x = "paraparaparadise"
y = "paragraph"

def bi_gram(text,set):
    for i in range(len(text)-1):
        set.add(text[i]+text[i+1])
    return set
X = set()
Y = set()
X = bi_gram(x,X)
Y = bi_gram(y,Y)
print("06 X: ",X)
print("06 Y: ",Y)

XY_union = X | Y
XY_intersection = X & Y
XY_difference = X - Y
print("06 和集合: ",XY_union)
print("06 積集合: ",XY_intersection)
print("06 差集合: ",XY_difference)

print("06 'se'がXに含まれているか： ",{'se'} <= X)
print("06 'se'がYに含まれているか： ",{'se'} <= Y)
print("\n")

#07. テンプレートによる文生成
def sen(x,y,z):
    l = str(x) + "時の" + str(y) + "は" + str(z)
    return l

print("07: ",sen(12,"気温",22.4))
print("\n")

#08. 暗号文
def cipher(sen):
    l = ""
    for i in range(len(sen)):
        if sen[i].islower() :
            l += chr(219 - ord(sen[i]))
        else:
            l += sen[i]
    return l

sen = "Hello World!"
print("08 暗号化：　",cipher(sen))
print("08 復号化：　",cipher(cipher(sen)))
print("\n")

#09. Typoglycemia
import random
def Typoglycemia(sen):
    sen = sen.split(' ')
    l = ""
    for i in range(len(sen)):
        if len(sen[i]) > 4 :
            sen_ = random.sample(sen[i][1:-1],len(sen[i][1:-1]))
            if i != 0 :
                l += ' ' + sen[i][0] + ''.join(sen_) + sen[i][-1]
            else :
                l += sen[i][0] + ''.join(sen_) + sen[i][-1]
        else:
            if i != 0 :
                l += ' ' + sen[i]
            else:
                l += sen[i]
    return l

sen = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print("09: ",Typoglycemia(sen))
