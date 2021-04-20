# 07_テンプレートによる文生成

def tp(x, y, z):
    s = str(x) + "時の" + str(y) + "は" + str(z)
    return s


print(tp(12, "気温", 22.4))
