# 09_Typoglycemia

import random

def ran(str):
    
    lst = str.split()
    
    for i in range(len(lst)):
        str1 = lst[i]
        if len(str1) > 4:
            str1 = str1[:1] + ''.join(random.sample(str1[1:-1], len(str1)-2)) + str1[-1:]
            lst[i] = str1
            
    ans = ' '.join(lst)
    
    return ans


S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(ran(S))
