# 09_Typoglycemia

"""
スペースで区切られた単語列に対して、各単語の先頭と末尾は残し、それ以外の文字の順序をランダムに並び替える。
長さ4以下の単語は並び替えない。
"""

import random

def typoglycemia(Input):
    
    lst = Input.split()
    
    for i in range(len(lst)):
        str_old = lst[i]
        if len(str_old) > 4:
            str_new = str_old[0] + ''.join(random.sample(str_old[1:-1], len(str_old[1:-1]))) + str_old[-1]
            lst[i] = str_new
            
    ans = ' '.join(lst)
    
    return ans


S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(S))


