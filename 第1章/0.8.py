def cipher(str):
  rep = [chr(219 - ord(x)) if x.islower() else x for x in str]

  return ''.join(rep)

message = 'If you find a path with no obstacles, it probably doesn’t lead anywhere.'
message = cipher(message)
print('加密:', message)
message = cipher(message)
print('解密:', message)