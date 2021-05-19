import gensim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

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
Z = linkage(vec,method='ward')
dendrogram(Z, labels=cot)
plt.title("Dendrogram")
plt.show()
