#03. 圆周率Permalink
#给定语句”Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
#以单词为单位分割该语句，并创建一个列表，顺次记录该语句中各个单词的长度（即字符数）。

#split() 通过指定分隔符对字符串进行切片
import re

string='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
string = re.sub(r'[^\w\s]', '', string).split()
print(string)
print([len(i) for i in string])
