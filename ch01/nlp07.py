def sentence_generator(x, y, z):
   return str(x) + "時の" + y + "は" + str(z)

print(sentence_generator(x=12, y="気温", z=22.4))