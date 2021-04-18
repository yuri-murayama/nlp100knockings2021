str1 = 'パトカー'
str2 = 'タクシー'

result = ''.join([i + j for i, j in zip(str1, str2)])

print(result)