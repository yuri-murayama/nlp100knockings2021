import pandas as pd
df = pd.read_csv('./NewsAggregatorDataset/newsCorpora.csv', sep='\t', header=None, names=['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP'])
extracted = df[df['PUBLISHER'].isin(['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail'])]
shuffled = extracted.sample(frac=1)
ctitle = shuffled[['CATEGORY','TITLE']]
ctitle[:4*len(shuffled)//5+1:].to_csv('train.txt',sep='\t')
ctitle[4*len(shuffled)//5+1:9*len(shuffled)//10+1:].to_csv('valid.txt',sep='\t')
ctitle[9*len(shuffled)//10+1::].to_csv('test.txt',sep='\t')
print(df['CATEGORY'].value_counts())
