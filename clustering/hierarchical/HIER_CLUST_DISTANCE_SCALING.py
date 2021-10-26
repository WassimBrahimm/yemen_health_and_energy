from clustering.connect_sf import cs
from sklearn.preprocessing import StandardScaler

# Import standard libraries
import pandas as pd
import numpy as np

# Import the hierarchical clustering algorithm
from sklearn.cluster import AgglomerativeClustering

# Import functions created for this course
from functions import *
from functions.clustering_functions import plot_dendrogram, display_factorial_planes

#todo define number of clusters:
n_clusters=10


query = """
SELECT
FACILITY_ID,
dist_AIRBORNE_2015,
dist_AIRBORNE_2016,
dist_ground_2015,
dist_ground_2016,
FACILITY_TYPE_MODELLED,
ON_GRID_AVL,
URBAN,
ON_GRID,
SOLAR_ONL,
DIESEL_ONL
from clean_cluster_facility_test_tt
"""
cs.execute(query)
data_set = cs.fetch_pandas_all()
X = data_set[[
    'DIST_AIRBORNE_2015',
    'DIST_AIRBORNE_2016',
    'DIST_GROUND_2015',
    'DIST_GROUND_2016',
    # 'FACILITY_TYPE_MODELLED',
    # 'ON_GRID_AVL',
    # 'URBAN',
    # 'ON_GRID',
    # 'SOLAR_ONL',
    # 'DIESEL_ONL'
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
X_scaled_clustered = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
X_scaled_clustered['cluster'] = clusters
# export the data sets to csv file with cluster column
print('1')
X_scaled_clustered.to_csv('csv_export/clusters_'+str(n_clusters)+'.csv', index=False)
print(X_scaled_clustered.head())
print('2')
#
# todo analyse the clustering results

print(X_scaled_clustered["cluster"].value_counts())
# Show a dendrogram, for the clusters 1 by 1
from scipy.cluster.hierarchy import linkage, fcluster


# for index in range(0,n_clusters):
#     sample = X_scaled_clustered[X_scaled_clustered.cluster == index]
#     Z = linkage(sample, 'ward')
#     names = sample.index
#     plot_dendrogram(Z, names, figsize=(10, 20))

from sklearn.decomposition import PCA

# Create a PCA model to reduce our data to 2 dimensions for visualisation
pca = PCA(n_components=2)
pca.fit(X_scaled)

# Transfor the scaled data to the new PCA space
X_reduced = pca.transform(X_scaled)
display_factorial_planes(X_reduced, 2, pca, [(0, 1)], illustrative_var=clusters, alpha=0.9)
