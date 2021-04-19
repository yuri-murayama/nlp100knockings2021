str1 = "パトカー"
str2 = "タクシー"
str_list = []
for i in range(4):
    str_list += str1[i] + str2[i]

print(''.join(str_list))