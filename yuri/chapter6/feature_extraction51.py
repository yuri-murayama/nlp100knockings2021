from transformers import pipeline
import pandas as pd
import numpy as np

## Huggingface Transformersのfeature-extractionを使用
fe = pipeline("feature-extraction")

def f(x):
    return pd.Series(fe(x)[0][0])

for mode in ['train', 'valid', 'test']:
    df = pd.read_table("data/%s.txt" % mode)
    df = df['TITLE'].apply(f)
    df.to_csv("data/%s.feature.txt" % mode, header= False, index=False, sep='\t')