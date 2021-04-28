## 参考：https://radimrehurek.com/gensim/models/word2vec.html
import gensim
wv = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True)

print('"United_States" vector: ', wv['United_States'])
print('Similarity of "United_States" and "U.S.": ', wv.similarity('United_States', 'U.S.'))
print('10 Most similar words of "United_States": ', wv.most_similar('United_States', topn=10))
print('"Spain"-"Madrid"+"Athens"= ', wv.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))

## 実行結果
'''
"United_States" vector:  [-3.61328125e-02 ... -2.67333984e-02]
Similarity of "United_States" and "U.S.":  0.73107743
10 Most similar words of "United_States":  [('Unites_States', 0.7877248525619507), ('Untied_States', 0.7541370987892151), ('United_Sates', 0.7400724291801453), ('U.S.', 0.7310774326324463), ('theUnited_States', 0.6404393911361694), ('America', 0.6178410053253174), ('UnitedStates', 0.6167312264442444), ('Europe', 0.6132988929748535), ('countries', 0.6044804453849792), ('Canada', 0.601906955242157)]
"Spain"-"Madrid"+"Athens"=  [('Greece', 0.6898480653762817), ('Aristeidis_Grigoriadis', 0.560684859752655), ('Ioannis_Drymonakos', 0.5552908778190613), ('Greeks', 0.545068621635437), ('Ioannis_Christou', 0.5400862097740173), ('Hrysopiyi_Devetzi', 0.5248445272445679), ('Heraklio', 0.5207759737968445), ('Athens_Greece', 0.516880989074707), ('Lithuania', 0.5166865587234497), ('Iraklion', 0.5146791338920593)]
'''