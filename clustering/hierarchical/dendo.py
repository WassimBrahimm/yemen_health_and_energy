from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import normalize
import scipy.cluster.hierarchy as shc
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

from functions.clustering_functions import plot_dendrogram,display_factorial_planes

original_data = pd.read_csv(
    '/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/facilities.csv')

X = original_data[[

    'MIN_AIR_2015',
    'MIN_AIR_2016',
    'MIN_GROUND_2015',
    'MIN_GROUND_2016',
    'FACILITY_TYPE',
    'ON_GRID_AVL',
    'URBAN',
    'ON_GRID',
    'SOLAR_ONL',
    'SOLAR_INC',
    'DIESEL_ONL'
]]
print(X.head())
X = X.fillna(X.mean())
# Import the sklearn function
from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Create a hierarchical clustering model
hiercluster = AgglomerativeClustering(affinity='euclidean', linkage='ward', compute_full_tree=True)
# Fit the data to the model and determine which clusters each data point belongs to:
hiercluster.set_params(n_clusters=8)
clusters = hiercluster.fit_predict(X_scaled)
np.bincount(clusters) # count of data points in each cluster
print(np.bincount(clusters) )
# Add cluster number to the original data
# X_scaled_clustered = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
# X_scaled_clustered['cluster'] = clusters
#
# X_scaled_clustered.head()
# # Find the size of the clusters
# X_scaled_clustered["cluster"].value_counts()

# Show a dendrogram, just for the smallest cluster
# from scipy.cluster.hierarchy import linkage, fcluster
# sample = X_scaled_clustered
# Z = linkage(sample, 'ward')
# names = sample.index
# plot_dendrogram(Z, names, figsize=(20,10))
# from sklearn.decomposition import PCA
#
# # Create a PCA model to reduce our data to 2 dimensions for visualisation
# pca = PCA(n_components=2)
# pca.fit(X_scaled)
#
# # Transfor the scaled data to the new PCA space
# X_reduced = pca.transform(X_scaled)
# display_factorial_planes(X_reduced, 2, pca, [(0,1)], illustrative_var = clusters, alpha = 0.8)
# print(X_scaled_clustered["cluster"].value_counts())
