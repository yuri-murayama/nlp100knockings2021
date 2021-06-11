import os
import pandas as pd
import numpy as np

df = pd.read_table("NewsAggregatorDataset/newsCorpora.csv", header=None, names=('ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'))
# discard 210713～210723 from newsCorpora.csv
df = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
df = df.loc[:, ['TITLE', 'CATEGORY']]
train, valid, test = np.split(df.sample(frac=1, random_state=0), [int(.8*len(df)), int(.9*len(df))])

data_dict = {'train':train, 'valid':valid, 'test':test}

os.makedirs("data", exist_ok=True)
for k, v in data_dict.items():
    v.to_csv("data/%s.txt" % k, index=False, sep='\t')
    print(k, v['CATEGORY'].value_counts())
