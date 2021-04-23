import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('train.feature.txt', sep='\t')
columns = df.columns.values
X = df[columns[2:]]
Y = df['CATEGORY']
#0:b = business, 1:e = entertainment, 2:m = health, 3:t = science and technology
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 52.learning
#lr = LogisticRegression()
#lr.fit(X_train, Y_train)

#print("coefficient = ", lr.coef_)
#print("intercept = ", lr.intercept_)

#pickle.dump(lr, open('model.sav', 'wb'))

# 53-54.predict
lr = pickle.load(open('model.sav', 'rb'))
Y_pred_train = lr.predict(X_train)
Y_pred_test = lr.predict(X_test)

print('train: accuracy = ', accuracy_score(y_true=Y_train, y_pred=Y_pred_train))
print('test: accuracy = ', accuracy_score(y_true=Y_test, y_pred=Y_pred_test))
