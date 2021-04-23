import random

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."
s = s.strip('.').split()
sover4 = [x for x in s if len(x)>4]

result = ''
while len(sover4) > 0:
    i = random.randrange(0,len(sover4))
    result += sover4[i] + ' '
    del sover4[i]

print(result)
