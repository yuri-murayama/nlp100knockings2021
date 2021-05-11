import pickle
import pandas as pd
import numpy as np

def prediction(model, x):
    pred = model.predict(x)
    print('prediction:', pred)
    
    return pred

lr = pickle.load(open('model.sav', 'rb'))

filename = ['train','valid','test']
for f in filename:
    print(f,'==>')
    feature_df = pd.read_csv('./data/'+f+'.feature.txt', sep='\t')
    pred = prediction(lr, feature_df)
    np.save('./data/'+f+'.prediction.npy',pred, allow_pickle=True)
