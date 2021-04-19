str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split()

one = [1, 5, 6, 7, 8, 9, 15, 16, 19]

ans_dict = {}
for i, word in enumerate(list):
    if i + 1 in one:
        ans_dict[word[:1]] = i + 1
    else:
        ans_dict[word[:2]] = i + 1

print(ans_dict)