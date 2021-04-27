# データの入手・整形
# 参考：https://note.nkmk.me/python-sklearn-train-test-split/
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./NewsAggregatorDataset/newsCorpora.csv', sep='\t', header=None, names=['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP'])

# データの抽出
ex = df[df['PUBLISHER'].isin(['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail'])]

# 事例の並び替え
# sfl = ex.sample(frac=1)

# データの分割、並び替え
train, valid_test = train_test_split(ex,test_size=0.2,shuffle=True,random_state=56,stratify=ex['CATEGORY'])
valid, test = train_test_split(valid_test,test_size=0.5,shuffle=True,random_state=56,stratify=valid_test['CATEGORY'])

# 出力
train.to_csv('train.txt',sep='\t',index=False)
valid.to_csv('valid.txt',sep='\t',index=False)
test.to_csv('test.txt',sep='\t',index=False)

# 各カテゴリ事例数確認
print(train['CATEGORY'].value_counts())
print(valid['CATEGORY'].value_counts())
print(test['CATEGORY'].value_counts())
