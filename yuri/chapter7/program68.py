import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pickle

with open('data/country_vec.pickle', 'rb') as f:
    country_vec = pickle.load(f)

plt.figure(figsize=(32, 18))
l = linkage(list(country_vec.values()), method='ward')
dendrogram(l, labels=list(country_vec.keys()), leaf_font_size=10)
plt.savefig('ward.png')