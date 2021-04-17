s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list=s.split()

list=[a.strip(",") for a in list]
list=[a.strip(".") for a in list]

lenlist=[len(a) for a in list]

print(lenlist)
