import gensim

wvs = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)

wf = open('./data/result_64.txt',mode='w')
with open('./data/questions-words.txt') as rf:
    while True:
        l = rf.readline()
        words = l.split(' ')
        if len(words) > 2:
            vec = wvs[words[1]] - wvs[words[0]] + wvs[words[2]]
            sim = wvs.similar_by_vector(vec,topn=1)
            wf.write(l+' '+str(sim[0][0])+' '+str(sim[0][1])+'\n')
        elif not l:
            break
