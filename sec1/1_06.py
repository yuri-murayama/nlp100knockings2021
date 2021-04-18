def n_gram(n,target):
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(n_gram(2,str1))
Y = set(n_gram(2,str2))

print('X:',X)
print('Y:',Y)

print('和集合:',X.union(Y))
print('積集合',X.intersection(Y))
print('差集合:',X.difference(Y))

print('seがXに含まれるか:',('se' in X))
print('seがYに含まれるか:','se' in Y)
    