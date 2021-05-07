s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
scut = s.strip('.').split()
c1 = [0, 4, 5, 6, 7, 8, 14, 15, 18]
snew = {}
for i in range(len(scut)):
    if i in c1:
        snew[scut[i][:1]] = i+1
    else:
        snew[scut[i][:2]] = i+1
print(snew)
