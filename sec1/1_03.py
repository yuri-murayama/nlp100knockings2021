import re
target = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

str1 = re.sub('[,.]','',target)

target_list = str1.split(' ')

mojisu_list = []

for ii in target_list:
    mojisu_list.append(len(ii))

print(mojisu_list)
