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
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)
print('Xにseが含まれるか:', {('se')} <= X)
print('Yにseが含まれるか:', {('se')} <= Y)