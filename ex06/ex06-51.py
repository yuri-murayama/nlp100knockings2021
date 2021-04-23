import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

def feature(s):
    df = pd.read_csv(s+'.txt', sep='\t')
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['TITLE'])

    label_encoder = LabelEncoder()
    Y = label_encoder.fit_transform(df['CATEGORY'])

    #print('Vocabulary size: {}'.format(len(vectorizer.vocabulary_)))
    #print('Vocabulary content: {}'.format(vectorizer.vocabulary_))

    X_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
    Y_df = pd.DataFrame(Y).rename(columns={0:'CATEGORY'})
    vec_df = Y_df.join(X_df)
    print(s,"\n",vec_df.head(5))
    vec_df.to_csv(s+'.feature.txt',sep='\t')

feature("train")
feature("valid")
feature("test")
