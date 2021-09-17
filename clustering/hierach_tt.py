# %matplotlib inline
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import numpy as np
from connect_sf import cs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.vq import whiten

cs.execute("SELECT * FROM demo_db.public.clean_cluster_facility;")
df = cs.fetch_pandas_all()
df = df.reset_index()
scaled_data = whiten(df)

# # sns.clustermap(df)
# cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
# cluster.fit_predict(df)