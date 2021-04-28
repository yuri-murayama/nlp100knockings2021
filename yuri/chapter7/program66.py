import gensim
import pandas as pd
wv = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True)

def f(x):
    return wv.similarity(x['Word 1'], x['Word 2'])

df = pd.read_csv('data/combined.csv')
df['wv'] = df.apply(f, axis=1)
## スピアマン相関係数を計算
print(df[['wv', 'Human (mean)']].corr(method="spearman"))

## 実行結果
'''
                    wv  Human (mean)
wv            1.000000      0.700017
Human (mean)  0.700017      1.000000
'''