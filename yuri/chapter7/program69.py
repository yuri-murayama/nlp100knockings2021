import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle

with open('data/country_vec.pickle', 'rb') as f:
    country_vec = pickle.load(f)

vec_embedded = TSNE(n_components=2, random_state=0).fit_transform(list(country_vec.values()))
plt.figure(figsize=(20, 20))
plt.scatter(vec_embedded[:, 0], vec_embedded[:, 1])
for i, label in enumerate(country_vec.keys()):
    plt.annotate(label, (vec_embedded[i, 0], vec_embedded[i, 1]))
plt.savefig('t-SNE.png')