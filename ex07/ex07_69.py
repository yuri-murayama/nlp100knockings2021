import gensim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

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
tsne = TSNE()
tsne.fit(vec)
plt.scatter(tsne.embedding_[:, 0], tsne.embedding_[:, 1])
plt.title("t-SNE")
for (x, y), name in zip(tsne.embedding_, cot):
    plt.annotate(name, (x, y))
plt.show()
