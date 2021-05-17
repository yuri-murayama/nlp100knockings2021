import gensim

wvs = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)

vec = wvs['Spain'] - wvs['Madrid'] + wvs['Athens']
print(wvs.similar_by_vector(vec))
