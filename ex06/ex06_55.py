import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

filename = ['train','valid','test']
for f in filename:
    print(f,'==>')
    df = pd.read_csv('./data/'+f+'.txt', sep='\t')
    pred = np.load('./data/'+f+'.prediction.npy', allow_pickle=True)
    print('confusion matrix:\n',confusion_matrix(df['CATEGORY'], pred))
