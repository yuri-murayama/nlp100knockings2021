# 07_テンプレートによる文生成


# 引数x, y, zを受け取り、「x時のyはz」と返す関数
def temp(x, y, z):
    s = str(x) + "時の" + str(y) + "は" + str(z)
    return s


x = 12
y = "気温"
z = 22.4

print(temp(x, y, z))
