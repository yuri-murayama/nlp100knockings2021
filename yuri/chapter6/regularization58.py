from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

feature, data = {}, {}
for mode in ['train', 'valid', 'test']:
    feature[mode] = pd.read_table("data/%s.feature.txt" % mode, header=None)
    data[mode] = pd.read_table("data/%s.txt" % mode)

acc_results = []
C = np.logspace(-5, 4, 10, base=10)
for c in tqdm(C):
    model = LogisticRegression(random_state=0, C=c, max_iter=1000).fit(feature['train'], data['train']['CATEGORY'])

    acc = []
    for mode in ['train', 'valid', 'test']:
        pred = model.predict(feature[mode])
        acc.append(accuracy_score(data[mode]['CATEGORY'], pred))
    acc_results.append(acc)

acc_results = np.array(acc_results).T

for acc, mode in zip(acc_results, ['train', 'valid', 'test']):
    plt.plot(C, acc, label=mode)
plt.ylim(0, 1.1)
plt.xscale('log')
plt.xlabel('C')
plt.ylabel('Acc')
plt.grid(True)
plt.legend()
plt.savefig('result.png')