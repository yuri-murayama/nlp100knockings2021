def n_gram(sentence, n):
    return [ sentence[i:i + n] for i in range(len(sentence) - n + 1)]

sentence= 'I am an NLPer'
gramwords = n_gram(sentence, 2)
print(gramwords)

word = sentence.split(' ')
gramword = n_gram(word, 2)
print(gramword)
