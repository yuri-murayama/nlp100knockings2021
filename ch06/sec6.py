
#50. データの入手・整形
import random
import numpy as np
from sklearn.model_selection import train_test_split

arr = []
with open("NewsAggregatorDataset/newsCorpora.csv",'r+')as f1:
    for lines in f1.readlines():
        col = lines.split('\t')
        #print(col)
        if col[3] in ['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail']:
            #print(col[3])
            arr.append(col)
arr2 = random.sample(arr,len(arr))
#print(len(arr2))
train, a = train_test_split(arr2, test_size=0.8)
test,valid = train_test_split(a,test_size=0.5)
#print(len(train))
#print(len(test))
#print(len(valid))

def write_file(filename,data):
    with open(filename,'w') as f:
        for l in data:
            text = l[1] + '\t' + l[4] + '\n'
            f.writelines(text)

write_file('train.txt',train)
write_file('valid.txt',valid)
write_file('test.txt',test)

import collections
print("train_data: ",collections.Counter([l[4] for l in train]))
print("valid_data: ",collections.Counter([l[4] for l in valid]))
print("test_data: ",collections.Counter([l[4] for l in test]))

#51. 特徴量抽出
#学習データ，検証データ，評価データから特徴量を抽出し，
#それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ．
#なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

train = pd.read_table('train.txt',header=None)
valid = pd.read_table('valid.txt',header=None)
test = pd.read_table('test.txt',header=None)

use_cols = ['TITLE', 'CATEGORY']

train.columns = use_cols
valid.columns = use_cols
test.columns = use_cols

#model = CountVectorizer() <- デフォルトだと１単語を飛ばしてしますようになっている
model = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
#正規表現　\b は単語の境界 \wは、単語構成文字　\w+ は1文字以上の単語構成文字の連続
#(?u)を指定することにより、Unicode文字列の意味での正規表現を扱う、という意味

model.fit(train['TITLE'])
model.fit(valid['TITLE'])
model.fit(test['TITLE'])

train_word = model.transform(train['TITLE'])
valid_word = model.transform(valid['TITLE'])
test_word = model.transform(test['TITLE'])

train_vector = pd.DataFrame(train_word.toarray())
valid_vector = pd.DataFrame(valid_word.toarray())
test_vector = pd.DataFrame(test_word.toarray())

#print(train)
#print(train_word)
#print(train_vector)

train_vector.to_csv('train.feature.txt', sep='\t', index=False, header=None)
valid_vector.to_csv('valid.feature.txt', sep='\t', index=False, header=None)
test_vector.to_csv('test.feature.txt', sep='\t', index=False, header=None)


#52. 学習
#51で構築した学習データを用いて，ロジスティック回帰モデルを学習せよ．
from sklearn.linear_model import LogisticRegression

X_train = pd.read_table('train.feature.txt',header=None)
y_train = pd.read_table('train.txt',header=None,usecols=[1])
y_train = y_train.values.ravel()

lr = LogisticRegression()
#print(X_train.shape)
print(y_train.shape)
lr.fit(X_train, y_train)

#53. 予測
#52で学習したロジスティック回帰モデルを用い，与えられた記事見出しからカテゴリとその予測確率を計算するプログラムを実装せよ．
print(lr.predict(X_train))

X_test = pd.read_table('test.feature.txt',header=None)
y_test = pd.read_table('test.txt',header=None,usecols=[1])


y_pred = lr.predict(X_test)
print(y_pred)

#54. 正解率の計測
#52で学習したロジスティック回帰モデルの正解率を，学習データおよび評価データ上で計測せよ．
from sklearn.metrics import accuracy_score

train_acc = accuracy_score(y_train,lr.predict(X_train))
test_acc = accuracy_score(y_test,y_pred)

print(train_acc)
print(test_acc)

#55. 混同行列の作成
#52で学習したロジスティック回帰モデルの混同行列（confusion matrix）を，学習データおよび評価データ上で作成せよ．
from sklearn.metrics import confusion_matrix

train_cm = confusion_matrix(y_train,lr.predict(X_train))
test_cm = confusion_matrix(y_test,y_pred)

print(train_cm)
print(test_cm)

#56. 適合率，再現率，F1スコアの計測
#52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ．
#カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能をマイクロ平均（micro-average）とマクロ平均（macro-average）で統合せよ．

#57. 特徴量の重みの確認
#52で学習したロジスティック回帰モデルの中で，重みの高い特徴量トップ10と，重みの低い特徴量トップ10を確認せよ．

#58. 正則化パラメータの変更
#ロジスティック回帰モデルを学習するとき，正則化パラメータを調整することで，学習時の過学習（overfitting）の度合いを制御できる
#異なる正則化パラメータでロジスティック回帰モデルを学習し，学習データ，検証データ，および評価データ上の正解率を求めよ．
#実験の結果は，正則化パラメータを横軸，正解率を縦軸としたグラフにまとめよ．

#59. ハイパーパラメータの探索
#学習アルゴリズムや学習パラメータを変えながら，カテゴリ分類モデルを学習せよ．
#検証データ上の正解率が最も高くなる学習アルゴリズム・パラメータを求めよ．
#また，その学習アルゴリズム・パラメータを用いたときの評価データ上の正解率を求めよ．
#学習アルゴリズムや学習パラメータを変えながら，カテゴリ分類モデルを学習せよ．検証データ上の正解率が最も高くなる学習アルゴリズム・パラメータを求めよ．また，その学習アルゴリズム・パラメータを用いたときの評価データ上の正解率を求めよ．
