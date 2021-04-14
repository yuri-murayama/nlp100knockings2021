def n_gram_generator(sentence, N):
    n_gram_list = []
    for i in range(len(sentence)-N+1):
        n_gram_list.append(sentence[i:i+N])
    return n_gram_list

if __name__=="__main__":
    sentence = "I am an NLPer"

    print("単語bi-gram：",n_gram_generator(sentence.split(), 2))
    print("文字bi-gram：",n_gram_generator(sentence, 2))