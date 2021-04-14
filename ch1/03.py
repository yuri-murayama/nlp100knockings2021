# 03_円周率

S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# スペースで区切る
lst = S.split() 

# .と,をとる
for i in range(len(lst)):
    lst[i] = lst[i].replace(".", "")
    lst[i] = lst[i].replace(",", "")


ans_lst = []

# 文字数をリストに入れる
for s in lst:
    ans_lst.append(len(s))

print(ans_lst)


