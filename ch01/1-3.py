str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = str.split()

ans_list = []
for i in range(len(list)):
    list[i] = list[i].replace(',','')
    list[i] = list[i].replace('.', '')
    ans_list.append(len(list[i]))

print(ans_list)