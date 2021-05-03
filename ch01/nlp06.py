from nlp05 import n_gram_generator

paradise = "paraparaparadise"
paragraph = "paragraph"

X = set(n_gram_generator(paradise, 2))
Y = set(n_gram_generator(paragraph, 2))

# X：{'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se'}
# Y：{'pa', 'ar', 'ra', 'ag', 'gr', 'ra', 'ap', 'ph'}

print("和集合：", X | Y)
print("積集合：", X & Y)
print("差集合(X-Y)：", X - Y)
print("差集合(Y-X)：", Y - X)
print("対称差集合：", X ^ Y)
print("seがXおよびYに含まれるか：","se" in (X or Y))

"""
和集合： {'ar', 'di', 'is', 'pa', 'se', 'ph', 'ag', 'ad', 'gr', 'ap', 'ra'}
積集合： {'pa', 'ra', 'ap', 'ar'}
差集合(X-Y)： {'se', 'ad', 'di', 'is'}
差集合(Y-X)： {'ag', 'ph', 'gr'}
対称差集合： {'ad', 'gr', 'di', 'is', 'ph', 'se', 'ag'}
seがXおよびYに含まれるか： True
"""
