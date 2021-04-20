#09. TypoglycemiaPermalink
#按下列要求编写程序:

#接收一个以空格为分隔符的单词序列作为输入
#对于在该序列中的每个单词：
#如果该单词的长度（字符数）不超过4，保持该单词不变；
#否则，
#保持该单词的首尾字符不变；
#随机打乱剩余字符的排列顺序。
#输入任意英文序列（例如”I couldn’t believe that I could actually understand what I was reading :
# the phenomenal power of the human mind. “），确认该程序的运行结果。

#要改变一个不可变的序列并返回一个新的打乱列表，请使用``sample(x, k=len(x))``。

import random
import re

string='I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind. '
string = re.sub(r'[^\w\s]', '', string).split()
res=[]
def TypoglycemiaPermalink(string):
    for w in string:
        if len(w)>4:
            w=w[:1]+''.join(random.sample(w[1:-1],len(w)-2))+w[-1:]
        res.append(w)
    return ' '.join(res)

print(TypoglycemiaPermalink(string))

