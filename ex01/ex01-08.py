def cipher(s):
    rtn = ''
    for c in s:
        if c.islower():
            rtn += chr(219-ord(c))
        else:
            rtn += c
    return rtn

def decypt(s):
    rtn = ''
    for c in s:
        if c.islower():
            rtn += chr(-(ord(c)-219))
        else:
            rtn += c
    return rtn

print(cipher("a.c.1912あ"))
print(decypt("z.x.1912あ"))
