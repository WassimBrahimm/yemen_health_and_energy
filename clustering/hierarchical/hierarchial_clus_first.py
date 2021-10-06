
from clustering.connect_sf import cs

# query="SELECT * FROM demo_db.public.clean_cluster_facility_test;"
query = """
SELECT

FACILITY_TYPE_MODELLED,
ON_GRID_AVL,
URBAN,
ON_GRID,
SOLAR_ONL,
DIESEL_ONL
from clean_cluster_facility_test
LIMIT 100;
"""
cs.execute(query)
df = cs.fetch_pandas_all()
# data_scaled = normalize(df)
# data_scaled = pd.DataFrame(data_scaled, columns=df.columns)
# plt.figure(figsize=(700, 700))
# plt.title("Dendrograms")
# print('I am here 0')
# dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
# print('I am here 1')
#
# # plt.show()
# plt.savefig('books_read.png')
# print('I am here 2')
# Hierarchical Clustering

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = df
# X = dataset.iloc[:, [3, 4]].values
from sklearn.preprocessing import normalize

data_scaled = normalize(dataset)
data_scaled = pd.DataFrame(data_scaled, columns=dataset.columns)
data_scaled.head()
X = data_scaled
X.head()
names = data_scaled.index
# Using the dendrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Facilities')
plt.ylabel('Euclidean distances')
plt.savefig('my_fig.png')
plt.show()

# Training the Hierarchical Clustering model on the dataset
# from sklearn.cluster import AgglomerativeClustering
#
# hc = AgglomerativeClustering(n_clusters=10, affinity='manhattan', linkage='complete')
# y_hc = hc.fit_predict(X)
#
# # Visualising the clusters
# # plt.figure(figsize=(1, 7))
# plt.show()
