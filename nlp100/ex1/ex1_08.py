#08. 密文Permalink
#实现函数cipher，使得它能够对给定字符串中的各个字符进行下列变换：

#对于任意一个小写英文字母c，将其置换成ASCII码为（219 - [c的ASCII码]）的字符；
#对于任意一个非小写英文字母的字符，不对其进行变换。
#使用该函数对英文信息进行加密与解密。

#字符转ascii数字 ord(字符）
#数字转字符 chr(数字)
#islower() 方法检测字符串是否由小写字母组成。

def cipher(string):
        res= ''.join((chr(219-ord(i)) if i.islower() else i for i in string))
        return res

string='Hello World'
print(cipher(string))
print(cipher(cipher(string)))
