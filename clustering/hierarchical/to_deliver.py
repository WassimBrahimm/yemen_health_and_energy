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

raw_data_frame = pd.read_csv(
    '/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/facilities.csv')

# 1. todo define number of clusters:
n_clusters = 7
# 2. todo remove the variables relevant to the clustering
selected_clustering_variables = [
    # 'FACILITY_ID',
    # 'GOV',
    # 'DISTRICT',
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
    # 'DIESEL_ONL',
    'DIESEL_INC'
]
clustering_frame = raw_data_frame[selected_clustering_variables]
clustering_frame = clustering_frame.fillna(clustering_frame.mean())

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(clustering_frame)
# Create a hierarchical clustering model
hier_cluster_model = AgglomerativeClustering(affinity='euclidean', linkage='ward', compute_full_tree=True)
# Fit the data to the model and determine which clusters each data point belongs to:
hier_cluster_model.set_params(n_clusters=n_clusters)
clusters = hier_cluster_model.fit_predict(X_scaled)
counts_per_cluster = (np.bincount(clusters))  # count of data points in each cluster


# convert numpy array to dictionary
dict_clust = dict(enumerate(counts_per_cluster.flatten(), 0))
for c in dict_clust:
    print('\ncluster {0} : {1} facilities.\n'.format(c, dict_clust.get(c)))
# ------------------------------------------------------------------------------------------------------------------------------
# Add cluster number to the original data
X_scaled_clustered = pd.DataFrame(raw_data_frame, columns=raw_data_frame.columns, index=raw_data_frame.index)
X_scaled_clustered['cluster'] = clusters

X_scaled_clustered.head()
# export the data sets to csv file with cluster column
X_scaled_clustered.to_csv('csv_export/clusters_' + str(n_clusters) + '.csv',sep=';', index=False)
#
# # print(X_scaled_clustered.head())
# # todo analyse the clustering results
#
# print(X_scaled_clustered["cluster"].value_counts())
# # Show a dendrogram, for the clusters 1 by 1
#
#
sample = clustering_frame
Z = linkage(clustering_frame, 'ward')
names = raw_data_frame['FACILITY_ID'].values
# plot_dendrogram(Z, names, figsize=(10, 20))
#
# Create a PCA model to reduce our data to 2 dimensions for visualisation
pca = PCA(n_components=2)
pca.fit(X_scaled)

# Transfor the scaled data to the new PCA space
X_reduced = pca.transform(X_scaled)
display_factorial_planes(X_reduced, 2, pca, [(0, 1)], illustrative_var=clusters, alpha=0.9)


print('*'*100)
print(type(X_reduced))
df = pd.DataFrame(data=X_reduced, columns=["column1", "column2"])
df.to_csv("plot.csv",index=False)
print('*'*100)
# display_factorial_planes(X_reduced, 2, pca, [(0, 1)], illustrative_var=clusters, alpha=0.9)
# # Add the cluster number to the original scaled data
# X_clustered = pd.DataFrame(X_scaled, index=clustering_frame.index, columns=clustering_frame.columns)
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
