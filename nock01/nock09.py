import random

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

l = s.split()

news = []

for x in l:
    if len(x) > 4 :
        newx = random.sample(x[1:-1],len(x)-2)
        x = x[0] + "".join(newx) + x[len(x)-1]

    news.append(x)

print(" ".join(news))

