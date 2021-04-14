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