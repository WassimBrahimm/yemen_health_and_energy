
from clustering.connect_sf import cs
# Import standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the kmeans algorithm
from sklearn.cluster import KMeans

# Import functions created for this course
# from functions import *
# query="SELECT * FROM demo_db.public.clean_cluster_facility_test;"
from functions.clustering_functions import display_factorial_planes, display_parallel_coordinates

query = """
SELECT
FACILITY_TYPE_MODELLED,
ON_GRID_AVL,
URBAN,
ON_GRID,
SOLAR_ONL,
DIESEL_ONL
from clean_cluster_facility_test
LIMIT 2500;
"""
cs.execute(query)
df = cs.fetch_pandas_all()
headers=df.head()
# Import the sklearn function
from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
# Create a k-means clustering model
kmeans = KMeans(init='random', n_clusters=5, n_init=10)

# Fit the data to the model
kmeans.fit(X_scaled)

# Determine which clusters each data point belongs to:
clusters =  kmeans.predict(X_scaled)


# Add cluster number to the original data
X_scaled_clustered = pd.DataFrame(X_scaled, columns=df.columns, index=df.index)
X_scaled_clustered['cluster'] = clusters

X_scaled_clustered.head()
# Run a number of tests, for 1, 2, ... num_clusters
# num_clusters = 50
# kmeans_tests = [KMeans(n_clusters=i, init='random', n_init=10) for i in range(1, num_clusters)]
# score = [kmeans_tests[i].fit(X_scaled).score(X_scaled) for i in range(len(kmeans_tests))]
#
# # Plot the curve
# plt.plot(range(1, num_clusters),score)
# plt.xlabel('Number of Clusters')
# plt.ylabel('Score')
# plt.title('Elbow Curve')

from sklearn.decomposition import PCA

# Create a PCA model to reduce our data to 2 dimensions for visualisation
pca = PCA(n_components=5)
pca.fit(X_scaled)

# Transfor the scaled data to the new PCA space
X_reduced = pca.transform(X_scaled)
# Convert to a data frame
X_reduceddf = pd.DataFrame(X_reduced, index=df.index, columns=['PC1','PC2'])
X_reduceddf['cluster'] = clusters
X_reduceddf.head()
centres_reduced = pca.transform(kmeans.cluster_centers_)
display_factorial_planes(X_reduced, 2, pca, [(0,1)], illustrative_var = clusters, alpha = 0.8)
plt.scatter(centres_reduced[:, 0], centres_reduced[:, 1],
            marker='x', s=169, linewidths=3,
            color='r', zorder=10)
# Add the cluster number to the original scaled data
X_clustered = pd.DataFrame(X_scaled, index=df.index, columns=df.columns)
X_clustered["cluster"] = clusters

# Display parallel coordinates plots, one for each cluster
display_parallel_coordinates(X_clustered, 3)

print('done')