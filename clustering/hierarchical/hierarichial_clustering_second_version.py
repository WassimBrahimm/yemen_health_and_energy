from clustering.connect_sf import cs
from sklearn.preprocessing import StandardScaler

# Import standard libraries
import pandas as pd
import numpy as np

# Import the hierarchical clustering algorithm
from sklearn.cluster import AgglomerativeClustering

# Import functions created for this course
from functions import *
from functions.clustering_functions import plot_dendrogram


#todo define number of clusters:
n_clusters=6


query = """
SELECT
KEY_CODE,
MIN_DISTANCE_AIRBORNE_2015,
MIN_DISTANCE_AIRBORNE_2016,
MIN_DISTANCE_GROUND_2015,
MIN_DISTANCE_GROUND_2016,
FACILITY_TYPE_MODELLED,
ON_GRID_AVL,
URBAN,
ON_GRID,
SOLAR_ONL,
DIESEL_ONL
from clean_cluster_facility_test
"""
cs.execute(query)
data_set = cs.fetch_pandas_all()
X = data_set[[
    'MIN_DISTANCE_AIRBORNE_2015',
    'MIN_DISTANCE_AIRBORNE_2016',
    'MIN_DISTANCE_GROUND_2015',
    'MIN_DISTANCE_GROUND_2016',
    'FACILITY_TYPE_MODELLED',
    'ON_GRID_AVL',
    'URBAN',
    'ON_GRID',
    'SOLAR_ONL',
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
X_scaled_clustered = pd.DataFrame(data_set, columns=X.columns, index=X.index)
X_scaled_clustered['cluster'] = clusters
# export the data sets to csv file with cluster column
X_scaled_clustered.to_csv('csv_export/clusters.csv', index=False)

# todo analyse the clustering results

print(X_scaled_clustered["cluster"].value_counts())
# Show a dendrogram, for the clusters 1 by 1
from scipy.cluster.hierarchy import linkage, fcluster


for index in range(0,n_clusters):
    sample = X_scaled_clustered[X_scaled_clustered.cluster == index]
    Z = linkage(sample, 'ward')
    names = sample.index
    plot_dendrogram(Z, names, figsize=(10, 20))
