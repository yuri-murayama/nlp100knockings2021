sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

sentence = sentence.replace(",","")
sentence = sentence.replace(".","")

print([len(word) for word in sentence.split()])