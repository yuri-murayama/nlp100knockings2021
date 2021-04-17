import re

s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

list=s.split()
jisho={}

list=[a.strip(",") for a in list]
list=[a.strip(".") for a in list]


num=[1,5,6,7,8,9,15,16,19]

for i in range(0,len(list)):
    if i+1 in num:
        jisho[i+1]=list[i][0]
    else:
        jisho[i+1]=list[i][0:2]


print(jisho)
