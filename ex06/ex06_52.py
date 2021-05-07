import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

train_df = pd.read_csv('./data/train.txt', sep='\t')
train_feature_df = pd.read_csv('./data/train.feature.txt', sep='\t')

lr = LogisticRegression(random_state=1, max_iter=10000)
lr.fit(train_feature_df, train_df['CATEGORY'])

#print("coefficient = ", lr.coef_)
#print("intercept = ", lr.intercept_)

pickle.dump(lr, open('model.sav', 'wb'))

