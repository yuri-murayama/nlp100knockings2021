import gensim

wvs = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)
print(wvs.similarity('United_States','U.S.'))
