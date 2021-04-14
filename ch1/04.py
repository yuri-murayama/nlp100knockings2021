# 04_元素記号

S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 単語に分解
lst = S.split()

# 先頭一文字を取るものの番号
num_lst = [1, 5, 6, 7, 8, 9, 15, 16, 19]

ans_d = {}
for i in range(len(lst)):
    if i+1 in num_lst:
        ans_d[lst[i][:1]] = i+1
    else:
        ans_d[lst[i][:2]] = i+1

print(ans_d)
