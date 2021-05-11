import numpy as np
import pandas as pd
from tqdm import trange
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


train_feature_df = pd.read_csv('./data/train.feature.txt', sep='\t')
valid_feature_df = pd.read_csv('./data/valid.feature.txt', sep='\t')
test_feature_df = pd.read_csv('./data/test.feature.txt', sep='\t')

train_df = pd.read_csv('./data/train.txt', sep='\t')
valid_df = pd.read_csv('./data/valid.txt', sep='\t')
test_df = pd.read_csv('./data/test.txt', sep='\t')

clst = np.linspace(0.5, 5.0, 10)
wlst = ['balanced', None]
slst = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']

best = {'accuracy':0.0, 'c':None, 'w':None, 's':None}

for i in trange(10, desc='c loop'):
    c = clst[i]
    for j in trange(2, desc='w loop', leave=False):
        w = wlst[j]
        for k in trange(5, desc='s loop', leave=False):
            s = slst[k]
            lr = LogisticRegression(C=c, class_weight=w, solver=s, random_state=1, max_iter=10000)
            lr.fit(train_feature_df, train_df['CATEGORY'])

            pred = lr.predict(valid_feature_df)
            acc = 100*accuracy_score(valid_df['CATEGORY'], pred)
            if best['accuracy'] < acc:
                best['accuracy'] = acc
                best['c'] = c
                best['w'] = w
                best['s'] = s

lr = LogisticRegression(C=best['c'], class_weight=best['w'], solver=best['s'], random_state=1, max_iter=10000)
lr.fit(train_feature_df, train_df['CATEGORY'])

pred = lr.predict(test_feature_df)
acc = 100*accuracy_score(test_df['CATEGORY'], pred)

print("c:{0}\nw:{1}\ns:{2}\naccuracy:{3}%".format(best['c'],best['w'],best['s'],acc))
