# 04_元素記号

import numpy as np

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

lst = str.split()

num = np.array([1, 5, 6, 7, 8, 9, 15, 16, 19])

ans_d = {}
for i in range(len(lst)):
    if i in (num-1):
        ans_d[lst[i][:1]] = i+1
    else:
        ans_d[lst[i][:2]] = i+1

print(ans_d)
