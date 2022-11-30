# # 1. todo: define number of clusters:
# from scipy.cluster.hierarchy import linkage
# from sklearn.preprocessing import StandardScaler
#
# from functions.clustering_functions import plot_dendrogram
#
# n_clusters = 7
# # 2. todo: remove the # to include a variable in the clustering
# selected_clustering_variables = [
#     # 'FACILITY_ID',
#     'FACILITY_TYPE',
#     'URBAN',
#     'MIN_AIR_2015',
#     'MIN_AIR_2016',
#     'MIN_GROUND_2015',
#     'MIN_GROUND_2016',
#     'ON_GRID',
#     'ON_GRID_AVL',
#     'SOLAR_ONL',
#     'SOLAR_INC',
#     'DIESEL_ONL',
#     'DIESEL_INC'
# ]
#
# import pandas as pd
#
# raw_data_frame = pd.read_csv('/Users/wassimbrahim/Desktop/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/facilities.csv')
# clustering_frame = raw_data_frame[selected_clustering_variables]
# clustering_frame = clustering_frame.fillna(clustering_frame.mean())
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(clustering_frame)
# import plotly.figure_factory as ff
# import numpy as np
#
# X = X_scaled
# fig = ff.create_dendrogram(X)
# # fig.update_layout(width=800, height=500)
# fig.show()
import matplotlib as mpl
from matplotlib.pyplot import cm
import numpy as np

cmap = cm.rainbow(np.linspace(0, 1, 10))

colors=[mpl.colors.rgb2hex(rgb[:3]) for rgb in cmap]
print(colors)