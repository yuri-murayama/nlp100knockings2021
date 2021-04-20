# 06_集合

def n_gram(n,str):
    ans = set()
    for i in range(0, len(str) - n + 1):
        ans.add(str[i:i + n])

    return ans


X = n_gram(2, "paraparaparadise")
Y = n_gram(2, "paragraph")

print("和集合: ", X | Y)
print("積集合: ", X & Y)
print("差集合(X-Y): ", X - Y)
print("差集合(Y-X): ", Y - X)

print("seがXに含まれるか: ", "se" in X)
print("seがYに含まれるか: ", "se" in Y)
