import gensim
from sklearn.cluster import KMeans

cot = []
wvs = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)

with open('./data/questions-words.txt',mode='r') as f:
    while True:
        l = f.readline()
        words = l.split(' ')
        if len(words) > 2:
            cot += [words[1],words[3].strip('\n')]
        elif l.startswith(': currency') or not l:
            break

cot = list(set(cot))
vec = [wvs[word] for word in cot]
cls = KMeans(n_clusters=5)
result = cls.fit(vec)
labels = cls.labels_
cluster_to_words = {0:[], 1:[], 2:[], 3:[], 4:[]}
for cluster_id, word in zip(labels, cot):
    cluster_to_words[cluster_id].append(word)

print(cluster_to_words)
