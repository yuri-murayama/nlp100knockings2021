#04. 元素记号Permalink
#给定语句 “Hi He Lied Because Boron Could Not Oxidize Fluorine.
# New Nations Might Also Sign Peace Security Clause. Arthur King Can.”

#以单词为单位分割该语句，从第1个、第5个、第6个、第7个、第8个、第9个、第15个、第16个、第19个单词中提取第一个字符，
# 并从其他单词中提取前两个字符。随后创建一个关联数组（dictonary对象或map对象），将提取出的字符串映射到各个相应单词在该语句中的位置。


import re

string='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
string = re.sub(r'[^\w\s]', '', string).split()
list=[1,5,6,7,8,9,15,16,19]
res={}

for i in range(len(string)):
    if i+1 in list:
        res[i + 1] = string[i][0]
    else:
        res[i + 1] = string[i][0:2]

print(res)


