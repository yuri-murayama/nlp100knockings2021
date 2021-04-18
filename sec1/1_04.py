import numpy as np
import re
target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

target = re.sub('[,.]','',target)

tango_list = target.split()

tango_jisyo = {}
number = np.array([1, 5, 6, 7, 8, 9, 15, 16, 19])


for i in range(len(tango_list)):
    if i in (number - 1):
        tango = tango_list[i][:1]
    else:
        tango = tango_list[i][:2]
    tango_jisyo.setdefault(tango,i+1)

print(tango_jisyo)
        
