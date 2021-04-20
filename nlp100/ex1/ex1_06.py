#06. 集合Permalink
#设由单词”paraparaparadise”和”paragraph”所生成的字符级bi-gram为分别为集合X和集合Y。
# 求这两个集合的并(union)、交(intersection)、差(difference)。此外，请检查集合X和Y中是否包含bi-gram “se”。

string1='paraparaparadise'
string2='paragraph'

def ngram(string,n):
    n_gram=[]
    for i in range(len(string)-1):
        n_gram.append(string[i]+string[i+1])

    return n_gram

X=set(ngram(string1,2))
Y=set(ngram(string2,2))

print(X | Y)
print(X & Y)
print(X - Y)

print('se' in X)
print('se' in Y)
