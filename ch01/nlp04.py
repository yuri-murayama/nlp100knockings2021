sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sentence = sentence.replace(",","").replace(".","")

first_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dct = {}

for i, word in enumerate(sentence.split(), start=1):
    if i in first_char:
        dct[word[0]] = i
    else:
        dct[word[:2]] = i

print(dct)
#出力結果
#{'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20#}
