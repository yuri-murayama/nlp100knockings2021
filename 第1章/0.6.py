def ngram(list,n):
    return [list[i:i+n] for i in range(len(list) - n + 1)]
str1 = 'paraparaparadise'
str2 = 'paragraph'
X = set(ngram(str1,2))
Y = set(ngram(str2,2))
union = X | Y
intersection = X & Y
difference = X - Y

print('X:', X)
print('Y:', Y)
print('并:', union)
print('交:', intersection)
print('差:', difference)
print('X是否包含se:', {('s', 'e')} <= X)
print('Y是否包含se:', {('s', 'e')} <= Y)