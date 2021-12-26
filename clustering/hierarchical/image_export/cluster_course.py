from sklearn.preprocessing import StandardScaler

# Import standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, fcluster

# Import the hierarchical clustering algorithm
from sklearn.cluster import AgglomerativeClustering

# Import functions created for displaying charts
from functions.clustering_functions import plot_dendrogram, display_factorial_planes, display_parallel_coordinates, \
    display_parallel_coordinates_centroids

# todo define number of clusters:
n_clusters = 3
path = '/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/german_cities_mean_temperture.csv'
data_set = pd.read_csv(path, delimiter=',')

X1 = data_set[[
    'City',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]]
X = data_set[[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]]

X = X.fillna(X.mean())
#
# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Create a hierarchical clustering model
hiercluster = AgglomerativeClustering(affinity='euclidean', linkage='ward', compute_full_tree=True)
# Fit the data to the model and determine which clusters each data point belongs to:
hiercluster.set_params(n_clusters=n_clusters)
clusters = hiercluster.fit_predict(X_scaled)
counts_per_cluster = (np.bincount(clusters))  # count of data points in each cluster

# Add cluster number to the original data
X_scaled_clustered = pd.DataFrame(X1, columns=X1.columns, index=X1.index)
X_scaled_clustered['cluster'] = clusters
# export the data sets to csv file with cluster column
X_scaled_clustered.to_csv('clusters_' + str(n_clusters) + '.csv', index=False)

# print(X_scaled_clustered.head())
# todo analyse the clustering results

print(X_scaled_clustered["cluster"].value_counts())
# Show a dendrogram, for the clusters 1 by 1

# #
# for index in range(0,n_clusters):
#     sample = X_scaled_clustered[X_scaled_clustered.cluster == index]
#     Z = linkage(sample, 'ward')
#     names = sample.index
#     plot_dendrogram(Z, names, figsize=(10, 20))


# Create a PCA model to reduce our data to 2 dimensions for visualisation
pca = PCA(n_components=2)
pca.fit(X_scaled)
cities = X1['City'].values
f = []
for city in cities:
    if city == 'Frankfurt':
        f.append('Ffm')
    elif city == 'Freiburg':
        f.append('Frei')
    else:
        f.append(city[0:2])
print(f)
cities=f
# Transform the scaled data to the new PCA space
X_reduced = pca.transform(X_scaled)
# print('*******'*10)
#
# print(X_reduced)
# print('*******'*10)
# print(X_scaled)
# print('*******'*10)

display_factorial_planes(X_reduced, 2, pca, [(0, 1)], labels=cities, illustrative_var=clusters, alpha=0.9)
# # Add the cluster number to the original scaled data
# X_clustered = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)
# X_clustered["cluster"] = clusters
#
# # Display parallel coordinates plots, one for each cluster
# display_parallel_coordinates(X_clustered, n_clusters)
# means = X_clustered.groupby(by="cluster").mean()
# # boxplot plot
# display_parallel_coordinates_centroids(means.reset_index(), n_clusters)
# X_clustered.boxplot(by="cluster")
# # X_clustered.boxplot(by="cluster", figsize=(500, 400), layout=(11, 11))
# # plt.show()
# plt.savefig('/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/image_export/img.png')
# print('done')
