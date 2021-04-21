def n_gram_generator(sentence, N):
    n_gram_list = []
    for i in range(len(sentence)-N+1):
        n_gram_list.append(sentence[i:i+N])
    return n_gram_list

if __name__=="__main__":
    sentence = "I am an NLPer"

    print("単語bi-gram：",n_gram_generator(sentence.split(), 2))
    print("文字bi-gram：",n_gram_generator(sentence, 2))
#単語bi-gram： [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
#文字bi-gram： ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
