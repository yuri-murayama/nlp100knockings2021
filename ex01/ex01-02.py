s1 = 'パトカー'
s2 = 'タクシー'
print(''.join([x+s2[s1.index(x)] for x in s1]))
