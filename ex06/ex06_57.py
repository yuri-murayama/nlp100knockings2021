import pickle
import pandas as pd
import mglearn
import matplotlib.pyplot as plt

model = pickle.load(open('model.sav', 'rb'))
df = pd.read_csv('./data/train.feature.txt', sep='\t')
columns = df.columns.values
categoly = ['bussiness', 'entertainment', 'health', 'science and technology']

for i in range(4):
    mglearn.tools.visualize_coefficients(model.coef_[i], columns, n_top_features=10)
    plt.title("top 10 feature ("+categoly[i]+")")
    plt.show()
