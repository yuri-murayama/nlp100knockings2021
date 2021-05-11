import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

filename = ['train','valid','test']
for f in filename:
    print(f,'==>')
    df = pd.read_csv('./data/'+f+'.txt', sep='\t')
    pred = np.load('./data/'+f+'.prediction.npy', allow_pickle=True)
    print('accuracy:',accuracy_score(df['CATEGORY'], pred))
