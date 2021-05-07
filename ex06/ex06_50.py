import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv('./NewsAggregatorDataset/newsCorpora.csv', sep='\t', header=None, names=['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP'])
extracted = df[df['PUBLISHER'].isin(['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail'])]
extracted = extracted[['CATEGORY','TITLE']]

train, val_test = train_test_split(extracted, test_size=0.2, shuffle=True, random_state=1, stratify=extracted["CATEGORY"])

valid, test = train_test_split(val_test, test_size=0.5, shuffle=True, random_state=1, stratify=val_test["CATEGORY"])

print(df['CATEGORY'].value_counts())

train.to_csv('./data/train.txt', sep="\t", index=None)
valid.to_csv('./data/valid.txt', sep="\t", index=None)
test.to_csv('./data/test.txt', sep="\t", index=None)
