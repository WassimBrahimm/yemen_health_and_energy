from clustering.connect_sf import cs
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
n_clusters = 15

query = """
SELECT
FACILITY_ID,
MIN_DISTANCE_AIRBORNE_2015 AS MIN_AIR_2015,
MIN_DISTANCE_AIRBORNE_2016 AS MIN_AIR_2016,
MIN_DISTANCE_GROUND_2015 AS MIN_GROUND_2015,
MIN_DISTANCE_GROUND_2016 AS MIN_GROUND_2016,
FACILITY_TYPE_MODELLED AS FACILITY_TYPE,
ON_GRID_AVL,
SOLAR_INC,
URBAN,
EA,
ON_GRID,
SOLAR_ONL,
DIESEL_ONL
from DEMO_DB.PUBLIC.CLEAN_CLUSTER_FACILITY_TEST
"""
cs.execute(query)
data_set = cs.fetch_pandas_all()
X1 = data_set[[
    'FACILITY_ID',
    'MIN_AIR_2015',
    'MIN_AIR_2016',
    'MIN_GROUND_2015',
    'MIN_GROUND_2016',
    'FACILITY_TYPE',
    'ON_GRID_AVL',
    'URBAN',
    'EA',
    'ON_GRID',
    'SOLAR_ONL',
    'SOLAR_INC',
    'DIESEL_ONL'
]]
X = data_set[[
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
X_scaled_clustered.to_csv('csv_export/clusters_' + str(n_clusters) + '.csv', index=False)



# print(X_scaled_clustered.head())
# todo analyse the clustering results

print(X_scaled_clustered["cluster"].value_counts())
# Show a dendrogram, for the clusters 1 by 1

#
# for index in range(0,n_clusters):
#     sample = X_scaled_clustered[X_scaled_clustered.cluster == index]
#     Z = linkage(sample, 'ward')
#     names = sample.index
#     plot_dendrogram(Z, names, figsize=(10, 20))


# Create a PCA model to reduce our data to 2 dimensions for visualisation
pca = PCA(n_components=2)
pca.fit(X_scaled)

# Transfor the scaled data to the new PCA space
X_reduced = pca.transform(X_scaled)
print(X_reduced)
display_factorial_planes(X_reduced, 2, pca, [(0, 1)], illustrative_var=clusters, alpha=0.9)
# Add the cluster number to the original scaled data
X_clustered = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)
X_clustered["cluster"] = clusters

# Display parallel coordinates plots, one for each cluster
display_parallel_coordinates(X_clustered, n_clusters)
means = X_clustered.groupby(by="cluster").mean()
# boxplot plot
display_parallel_coordinates_centroids(means.reset_index(), n_clusters)
X_clustered.boxplot(by="cluster")
# X_clustered.boxplot(by="cluster", figsize=(500, 400), layout=(11, 11))
# plt.show()
plt.savefig('/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/image_export/img.png')
print('done')
