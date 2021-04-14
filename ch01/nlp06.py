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