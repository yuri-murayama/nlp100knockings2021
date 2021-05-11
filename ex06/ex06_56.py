import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score


df = pd.read_csv('./data/test.txt', sep='\t')
pred = np.load('./data/test.prediction.npy', allow_pickle=True)
conmat = confusion_matrix(df['CATEGORY'], pred)

category = {0:'b', 1:'e', 2:'m', 3:'t'}
tprec = 0

for c in category.keys():
    print('category: ',category[c])
    prec = conmat[c,c] / sum(conmat[:,c]) * 100
    recall = conmat[c,c] / sum(conmat[c,:]) * 100
    
    print('precision score = ', prec, "%")
    print('recall score = ', recall, "%")
    print('f1 score = ', (2*prec*recall)/(recall+prec), "%")

print('\nmacro \t ===>')
print('precision score:',precision_score(df['CATEGORY'], pred, average='macro'))
print('recall score:',recall_score(df['CATEGORY'], pred, average='macro'))
print('f1 score:',f1_score(df['CATEGORY'], pred, average='macro'))

print('\nmicro \t ===>')
print('precision score:',precision_score(df['CATEGORY'], pred, average='micro'))
print('recall score:',recall_score(df['CATEGORY'], pred, average='micro'))
print('f1 score:',f1_score(df['CATEGORY'], pred, average='micro'))
