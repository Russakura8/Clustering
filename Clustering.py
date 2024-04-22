import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
from sklearn import cluster, mixture
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

with open('normdata.txt', 'r') as f:
    _data = f.read()

data = eval(_data)


with open('students.txt', 'r') as f:
    _data = f.read()

students = eval(_data)


data = np.array(data)



clustering = cluster.DBSCAN(min_samples=3, eps=2.16).fit(data)
#clustering = cluster.SpectralClustering().fit(data)
#clustering = cluster.AgglomerativeClustering(n_clusters=6).fit(data)
#clustering = cluster.KMeans(n_clusters=3).fit(data)
#clustering = cluster.OPTICS(min_samples=3, eps=1.5).fit(data)
#clustering = mixture.GaussianMixture(n_components = 3).fit(data)

labels = clustering.labels_
#labels = clustering.predict(data)

np.set_printoptions(threshold=np.inf)
#for i in range(len(labels)):
#    if labels[i] == 1:
#        print(students[i])

print(labels)
print(max(labels))
print(np.count_nonzero(labels == -1))

pca = PCA(n_components=2)
pca.fit(data)
data = pca.transform(data)
#print(data)

plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
plt.show()