def ngram(list,n):
    return [list[i:i+n] for i in range(len(list) - n + 1)]

str = "I am an NLPer"

word_bigram = ngram(str.split(),2)
char_bigram = ngram(str,2)

print("単語bi-gram:", word_bigram)
print("文字bi-gram:", char_bigram)