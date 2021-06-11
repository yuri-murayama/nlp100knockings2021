import pandas as pd
import numpy as np
import gensim
import string
wv = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True)

## 前処理で'-'だけは除去せずに空白に置き換えるため、punctuationから外しておく
p = string.punctuation.replace('-', '')

def f(x):
    x = x.translate(str.maketrans('', '', p))
    x = x.replace('-', ' ')
    x = np.array([wv[word] for word in x.split() if word in wv]).mean(axis=0)
    return pd.Series(x)

label_dict = {'b':0, 't':1, 'e':2, 'm':3}

for mode in ['train', 'valid', 'test']:
    df = pd.read_table(f"data/{mode}.txt")
    df_x = df['TITLE'].apply(f)
    df_x.to_csv(f"data/X_{mode}.txt", header= False, index=False, sep='\t')
    df_y = df['CATEGORY'].replace(label_dict)
    df_y.to_csv(f"data/Y_{mode}.txt", header= False, index=False)