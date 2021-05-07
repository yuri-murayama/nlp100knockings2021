import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

train_df = pd.read_csv('./data/train.txt', sep='\t')
valid_df = pd.read_csv('./data/valid.txt', sep='\t')
test_df = pd.read_csv('./data/test.txt', sep='\t')
    
vectorizer = TfidfVectorizer()
train_v = vectorizer.fit_transform(train_df['TITLE'])
valid_v = vectorizer.transform(valid_df['TITLE'])
test_v = vectorizer.transform(test_df['TITLE'])

train_vdf = pd.DataFrame(train_v.toarray(), columns=vectorizer.get_feature_names())
valid_vdf = pd.DataFrame(valid_v.toarray(), columns=vectorizer.get_feature_names())
test_vdf = pd.DataFrame(test_v.toarray(), columns=vectorizer.get_feature_names())

print("train:\n",train_vdf.head(5))
train_vdf.to_csv('./data/train.feature.txt', index=False, sep='\t')
valid_vdf.to_csv('./data/valid.feature.txt', index=False, sep='\t')
test_vdf.to_csv('./data/test.feature.txt', index=False, sep='\t')
