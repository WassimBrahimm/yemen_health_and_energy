# 1. todo: define number of clusters:
from scipy.cluster.hierarchy import linkage
from sklearn.preprocessing import StandardScaler

from functions.clustering_functions import plot_dendrogram

n_clusters = 7
# 2. todo: remove the # to include a variable in the clustering
selected_clustering_variables = [
    # 'FACILITY_ID',
    'FACILITY_TYPE',
    'URBAN',
    'MIN_AIR_2015',
    'MIN_AIR_2016',
    'MIN_GROUND_2015',
    'MIN_GROUND_2016',
    'ON_GRID',
    'ON_GRID_AVL',
    'SOLAR_ONL',
    'SOLAR_INC',
    'DIESEL_ONL',
    'DIESEL_INC'
]

import numpy as np

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


import pandas as pd

raw_data_frame = pd.read_csv('/Users/wassimbrahim/Desktop/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/facilities.csv')
clustering_frame = raw_data_frame[selected_clustering_variables]
clustering_frame = clustering_frame.fillna(clustering_frame.mean())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(clustering_frame)

iris = X_scaled
X = iris.data

# setting distance_threshold=0 ensures we compute the full tree.
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X)
plt.title("Hierarchical Clustering Dendrogram")
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.axhline(y=65.6, color='black', linestyle='--')

plt.show()

