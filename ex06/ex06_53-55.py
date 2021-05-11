import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score


def prediction(model, x, y):
    pred = model.predict(x)
    print('prediction:', pred)
    print('confusion matrix:\n',confusion_matrix(y, pred))
    print('accuracy:',accuracy_score(y, pred))

    return pred

def prec_recall_f1(tr, pred, ave='macro'):
    print('precision score:',precision_score(tr, pred, average=ave))
    print('recall score:',recall_score(tr, pred, average=ave))
    print('f1 score:',f1_score(tr, pred, average=ave))




lr = pickle.load(open('model.sav', 'rb'))

filename = ['train','valid','test']
for f in filename:
    print(f,'==>')
    df = pd.read_csv('./data/'+f+'.txt', sep='\t')
    feature_df = pd.read_csv('./data/'+f+'.feature.txt', sep='\t')
    pred = prediction(lr, feature_df, df['CATEGORY'])
    np.save('./data/'+f+'.prediction.npy',pred)
