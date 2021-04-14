import random
random.seed(2021)

def Typoglycemia(sentence):
    typoglycemia_sentence_list = []
    for word in sentence.split():
        if len(word) <= 4:
            typoglycemia_sentence_list.append(word)
        else:
            first = word[0]
            last = word[-1]
            mid_list = list(word[1:-1])
            random.shuffle(mid_list)
            shuffled_word = first + ''.join(mid_list) + last
            typoglycemia_sentence_list.append(shuffled_word)
    return " ".join(typoglycemia_sentence_list)

print(Typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))