import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix


def prediction(model,x,y):
    pred = model.predict(x)
    acc = accuracy_score(y_true=y, y_pred=pred)
    conmat = confusion_matrix(y_true=y, y_pred=pred)
    print('prediction:',pred)
    print('accuracy:',acc)
    print('confusion matrix:\n',conmat)


lr = pickle.load(open('model.sav', 'rb'))

filename = ['train','valid','test']
for f in filename:
    print(f,'==>')
    df = pd.read_csv('./data/'+f+'.txt', sep='\t')
    feature_df = pd.read_csv('./data/'+f+'.feature.txt', sep='\t')
    prediction(lr, feature_df, df['CATEGORY'])
