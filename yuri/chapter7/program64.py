import gensim
from tqdm import tqdm
wv = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True)

with open('data/questions-words.txt') as f:
    lines = f.readlines()

new_lines = []
for line in tqdm(lines):
    line = line.strip()
    if line.startswith(':'):
        new_lines.append(line)
    else:
        w = line.split()
        word, score = wv.most_similar(positive=[w[1], w[2]], negative=[w[0]], topn=1)[0]
        new_lines.append(line+' '+word+' '+str(score))

with open('data/analogy.txt', 'w') as f:
    f.write('\n'.join(new_lines))