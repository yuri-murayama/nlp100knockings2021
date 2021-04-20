#02. “shoe” + “cold” = “schooled”Permalink
#交错地将“shoe”和“cold”中的字符顺次拼接，以得到字符串“schooled”。

#zip() 函数用于将可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

#合并字符串 join()

string1='shoe'
string2='cold'
print(''.join((a+b for a,b in zip(string1,string2))))