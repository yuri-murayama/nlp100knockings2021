# 06_集合


# 文字bi-gramの作成
def ngram(Input):
    S = set()
    
    for i in range(len(Input) - 1):
        str = Input[i:i+2]
        S.add(str)
        
    return S


X = ngram("paraparaparadise")
Y = ngram("paragraph")

print("和集合: ", X | Y)
print("積集合: ", X & Y)
print("差集合(X-Y): ", X - Y)
print("差集合(Y-X): ", Y - X)

print("\'se\' in X: ", "se" in X)
print("\'se\' in Y: ", "se" in Y)
