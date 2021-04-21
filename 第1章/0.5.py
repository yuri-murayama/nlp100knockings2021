def ngram(n, lst):
  return list(zip(*[lst[i:] for i in range(n)]))

str = 'I am an NLPer'
words = ngram(2, str.split())
chars = ngram(2, str)

print('单词bi-gram:', words)
print('字符bi-gram:', chars)