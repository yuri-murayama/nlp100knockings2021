# 03_円周率

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

lst = str.split() 

for i in range(len(lst)):
    lst[i] = lst[i].replace(".", "")
    lst[i] = lst[i].replace(",", "")


ans_lst = []

for ii in lst:
    ans_lst.append(len(ii))

print(ans_lst)
