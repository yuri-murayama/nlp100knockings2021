import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


train_feature_df = pd.read_csv('./data/train.feature.txt', sep='\t')
valid_feature_df = pd.read_csv('./data/valid.feature.txt', sep='\t')
test_feature_df = pd.read_csv('./data/test.feature.txt', sep='\t')

train_df = pd.read_csv('./data/train.txt', sep='\t')
valid_df = pd.read_csv('./data/valid.txt', sep='\t')
test_df = pd.read_csv('./data/test.txt', sep='\t')

param = np.logspace(-5, 5, 11, base=10)

train_result = []
valid_result = []
test_result = []

for x in tqdm(param):
    lr = LogisticRegression(C=x, random_state=1, max_iter=10000)
    lr.fit(train_feature_df, train_df['CATEGORY'])

    # train
    train_pred = lr.predict(train_feature_df)
    train_result.append(100*accuracy_score(train_df['CATEGORY'], train_pred))

    # valid
    valid_pred = lr.predict(valid_feature_df)
    valid_result.append(100*accuracy_score(valid_df['CATEGORY'], valid_pred))

    # test
    test_pred = lr.predict(test_feature_df)
    test_result.append(100*accuracy_score(test_df['CATEGORY'], test_pred))

plt.plot(param, train_result, label = "train")
plt.plot(param, valid_result, label = "valid")
plt.plot(param, test_result, label = "test")
plt.xscale('log')
plt.xlabel("Inverse of regularization strength")
plt.ylabel("accuracy")
plt.legend()
plt.show()
