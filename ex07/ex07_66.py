import gensim
import csv
from scipy.stats import spearmanr

wvs = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)

human = []
machine = []
with open('./data/wordsim353/combined.csv') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\r\n")
    header = next(rows)
    for row in rows:
        human.append(float(row[2]))
        machine.append(wvs.similarity(row[0],row[1]))

correlation, pvalue = spearmanr(human, machine)
print(correlation)
        
