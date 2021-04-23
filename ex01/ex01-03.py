s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
snew = s.strip('.').split()
slen = [len(x) for x in snew]
print(slen)
