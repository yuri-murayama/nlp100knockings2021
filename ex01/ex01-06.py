def ngram(n,s):
    x = set()
    for i in range(0,len(s)-n+1):
        x.add(s[i:i+n])
    return x

s1 = "paraparaparadise"
s2 = "paragraph"

X = ngram(2,s1)
Y = ngram(2,s2)

print("union:", X | Y)
print("intersection:", X & Y)
print("difference:", X - Y)
