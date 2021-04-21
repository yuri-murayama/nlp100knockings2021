from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from bayes_opt import BayesianOptimization
import pandas as pd
import numpy as np

feature, data = {}, {}
for mode in ['train', 'valid', 'test']:
    feature[mode] = pd.read_table("data/%s.feature.txt" % mode, header=None)
    data[mode] = pd.read_table("data/%s.txt" % mode)

def get_score(C, solver):
    C = C_lst[int(np.round(C))]
    solver = solver_lst[int(np.round(solver))]
    #print(solver)
    model = LogisticRegression(random_state=0, C=C, solver=solver).fit(feature['train'], data['train']['CATEGORY'])
    pred = model.predict(feature['valid'])
    score = accuracy_score(data['valid']['CATEGORY'], pred)
    return score

C_lst = np.logspace(-5, 4, 10, base=10)
solver_lst = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
bounds = {
    'C': (-0.5, 9.49),
    'solver': (-0.5, 4.5)
}
## ベイズ最適化
opt = BayesianOptimization(get_score, bounds)
opt.maximize()

## 最適化したハイパーパラメータで評価
optimized_params = opt.max['params']
C = C_lst[int(np.round(optimized_params['C']))]
solver = solver_lst[int(np.round(optimized_params['solver']))]
model = LogisticRegression(random_state=0, C=C, solver=solver).fit(feature['train'], data['train']['CATEGORY'])
pred = model.predict(feature['test'])
score = accuracy_score(data['test']['CATEGORY'], pred)
print('Optimized C: ', C)
print('Optimized solver: ', solver)
print('Best test accuracy: ', score)

## 実行結果
'''
Optimized C:  1.0
Optimized solver:  newton-cg
Best test accuracy:  0.8695652173913043
'''