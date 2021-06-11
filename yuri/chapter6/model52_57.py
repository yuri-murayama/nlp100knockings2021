## 参考：https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

feature, data = {}, {}
for mode in ['train', 'valid', 'test']:
    feature[mode] = pd.read_table("data/%s.feature.txt" % mode, header=None)
    data[mode] = pd.read_table("data/%s.txt" % mode)

# ロジスティック回帰モデルを学習
model = LogisticRegression(random_state=0).fit(feature['train'], data['train']['CATEGORY'])

def predict_with_score(x):
    score = np.max(model.predict_proba(x), axis=1)
    return model.predict(x), score

## 正解率、混同行列 
for mode in ['train', 'test']:
    print('=== %s ===' % mode)
    pred, _ = predict_with_score(feature[mode])
    acc = accuracy_score(data[mode]['CATEGORY'], pred)
    print('Accuracy: ', acc)
    cm = confusion_matrix(data[mode]['CATEGORY'], pred)
    print('Confusion matrix:\n', cm)

## 適合率、再現率、F1スコア
print('\t\tb\te\tt\tm\tmicro\tmacro')
for func in [precision_score, recall_score, f1_score]:
    y_true = data['test']['CATEGORY']
    y_pred, _ = predict_with_score(feature['test'])
    s = func(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    s = np.append(s, func(y_true, y_pred, average='micro'))
    s = np.append(s, func(y_true, y_pred, average='macro'))
    s = np.vectorize(lambda x: str(np.round(x, decimals=2)))(s)
    print(func.__name__+'\t'+'\t'.join(s.tolist()))

## 特徴量の重み
for cl, co in zip(model.classes_, model.coef_):
    print(cl)
    print('Top 10', np.argsort(co)[::-1][:10])
    print('Top 10 Worst', np.argsort(co)[:10])

## 実行結果
'''
=== train ===
Accuracy:  0.8704901133914348
Confusion matrix:
 [[4079  184   48  176]
 [ 151 3995   33   56]
 [ 121   89  476   32]
 [ 316  151   25  739]]
=== test ===
Accuracy:  0.8590704647676162
Confusion matrix:
 [[513  25   4  27]
 [ 22 488   3   4]
 [ 11  14  63   4]
 [ 51  16   7  82]]
                b       e       t       m       micro   macro
precision_score 0.86    0.9     0.7     0.82    0.86    0.82
recall_score    0.9     0.94    0.53    0.68    0.86    0.76
f1_score        0.88    0.92    0.6     0.75    0.86    0.79
b
Top 10 [671 188 165 756  74 309 696 101 746 409]
Top 10 Worst [ 98 455 211 423 392 574 649 509 130 524]
e
Top 10 [464 574 149 159  98 413  14 505 354 130]
Top 10 Worst [226 661 188 260 256 165 543 558  51 746]
m
Top 10 [338 132  85  51 201 551 105 711  76 361]
Top 10 Worst [184 427  70 292 675 635 523 404 176 434]
t
Top 10 [370 108 157  12 250 223 638 618 564 260]
Top 10 Worst [671 293 544 354  13 612 742 665 756 183]
'''