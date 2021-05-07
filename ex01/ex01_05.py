def ngram(n,s):
    x = set()
    for i in range(0,len(s)-n+1):
        x.add(s[i:i+n])
    return x

print(ngram(2,'I am an NLPer'))
