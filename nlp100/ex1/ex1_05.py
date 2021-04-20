#5. n-gramPermalink
#实现一个函数，从给定的序列对象中（例如string或list）来生成n-gram。
# 使用这个函数从句子”I am an NLPer”中获得单词级别的bi-gram与字符级别的bi-gram。

#Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)

string='I am an NLPer'
def ngram(string,n):
    n_gram=[]
    for i in range(len(string)-1):
        n_gram.append(string[i]+string[i+1])

    return n_gram

word=string.split();
print(ngram(word,2))

letter=string.replace(' ','');
print(ngram(letter,2))