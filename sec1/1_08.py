def cipher(str):
      rep = [chr(219 - ord(x)) if x.islower() else x for x in str]
      
      return ''.join(rep)


print(cipher('I Am Cat.'))
print(cipher(cipher('I Am Cat.')))
