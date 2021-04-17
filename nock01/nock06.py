s1 = "paraparaparadise"
s2 = "paragraph"

X = []
Y = []

for i in range(0,len(s1)-1):
    X.append(s1[i:i+2])

for j in range(0,len(s2)-1):
    Y.append(s1[j:j+2])

X=set(X)
Y=set(Y)
print("X:", X)
print("Y:", Y)


print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)
print('Xに"se":', "se" in X)
print('Yに"se":', "se" in Y)
