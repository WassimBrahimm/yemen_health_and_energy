# you can change the colors  in the chosen palette
palette_1 = [
    '#001219',
    '#005F73',
    '#0A9396',
    '#94D2BD',
    '#E9D8A6',
    '#EE9B00',
    '#CA6702',
    '#BB3E03',
    '#AE2012',
    '#A4bD19',

]
palette_2 = [
    '#264653',
    '#2A9D8F',
    '#8AB17D',
    '#E9C46A',
    '#F4A261',
    '#E76F51',

]
palette_3 = [
    '#2C3532',
    '#0F6466',
    '#D8B08C',
    '#FFCB9A',
    '#D2E8E3',
    '#2C3532',
]

palette_4 = \
    [
        '#BB786B',
        '#FDF0D5',
        '#DF817A',
        '#D04A4D',
        '#336683',
        '#669BBC',
        '#76818E',
    ]
# 1. todo: introduce the CSV file name containing the data and uploaded under
#  "../../output/". make sure that the name is surrounded by "" or '' 
# and contains the extension .csv
file_name = 'facilities.csv'
# 2. todo: define the number of clusters:
n_clusters = 7
# 3. todo: remove the # to include a variable in the clustering.
# if you introduce new variables, make sure that you introduce the variable name 
# surrounded by ("") or ('') and a comma (,) between the names.
selected_clustering_variables = [
    # 'FACILITY_ID',
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
    'DIESEL_ONL',
    'DIESEL_INC'
]

# ------  Artwork adjustments --------------- Optional ------------------------#
# 4. todo: change palette_1 to palette_2, palette_3 or palette_4 for different
#  coloring of the PCA result. 
palette = palette_1
# 5. todo: refine the size of the marker size(by default it is 9) for the PCA chart.
#  depending on your own clustering it might be a better graphic if you adjust the size between [7-12]
marker_size = 9

"""This code cell contains all the imports used in the following code, and it defines functions for visualization. You should run it."""

from sklearn.preprocessing import StandardScaler
from IPython.display import SVG

# Import standard libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from scipy.cluster import hierarchy
import sys

sys.setrecursionlimit(2000)

# Import the hierarchical clustering algorithm
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

import seaborn as sns

# Import standard libraries
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.kaleido.scope.mathjax = None


def display_factorial_planes(X_projected, n_comp, pca, axis_ranks, labels=None, alpha=1, illustrative_var=None):
    '''Display a scatter plot on a factorial plane, one for each factorial plane'''

    # For each factorial plane
    my_data = pd.DataFrame(columns=['pc 1', 'pc 2'])
    for d1, d2 in axis_ranks:
        if d2 < n_comp:

            # Initialise the matplotlib figure

            # Display the points
            if illustrative_var is None:
                plt.scatter(X_projected[:, d1], X_projected[:, d2], alpha=alpha)
                pass
            else:
                illustrative_var = np.array(illustrative_var)
                for value in np.unique(illustrative_var):
                    selected = np.where(illustrative_var == value)
                    # plt.scatter(X_projected[selected, d1], X_projected[selected, d2], alpha=alpha, label=value)
                    x = pd.DataFrame(X_projected[selected, d1]).T
                    y = pd.DataFrame(X_projected[selected, d2]).T
                    df = pd.DataFrame()
                    df['pc 1'] = x
                    df['pc 2'] = y
                    df['pc 1'] = df['pc 1'].apply(lambda x: round(x, 4))
                    df['pc 2'] = df['pc 2'].apply(lambda x: round(x, 4))
                    df['cluster'] = int(value + 1)
                    my_data = pd.concat([my_data, df])

                my_data.to_csv('../../output/distances.csv', index=False)

    draw_scatter_plot()


def plot_dendrogram(Z, names, figsize=(10, 25)):
    '''Plot a dendrogram to illustrate hierarchical clustering'''
    fig = plt.figure(figsize=(10, 10))
    plt.title('Hierarchical Clustering Dendrogram', fontsize=20)
    plt.xlabel('Distance (ward)', fontsize=13)
    plt.ylabel('Country', fontsize=13)
    dendrogram(Z,
               labels=names,
               distance_sort=True,
               leaf_rotation=True,
               orientation='right',
               show_contracted=True,
               )
    plt.savefig("../../output/dendrogram.svg",  bbox_inches='tight', format="svg")


def draw_scatter_plot():
    clusters = {}
    for n in range(0, n_clusters):
        clusters[n + 1] = 'Cluster {}'.format(n + 1)
    df = pd.read_csv('../../output/distances.csv').dropna()
    df = df[df['cluster'].isin(clusters.keys())]
    df = df.dropna()
    pc1 = df["pc 1"]
    max_pc1 = pc1.max() * 1.1
    min_pc1 = pc1.min() * 1.3

    pc2 = df["pc 2"]
    max_pc2 = pc2.max() * 1.1
    min_pc2 = pc2.min() * 1.3

    y_boundry = max(abs(max_pc2), abs(min_pc2))
    fig = px.scatter(
        df,
        x='pc 1',
        y='pc 2',
        color=df['cluster'].map(clusters),
        range_x=[min_pc1, max_pc1],
        range_y=[min_pc2, max_pc2],
        color_discrete_sequence=palette,
        width=840,
        height=600
    )
    fig.for_each_trace(lambda t: t.update(name=t.name.split("=")[-1]))
    fig.update_layout(legend_title_text='')
    fig.update_traces(marker=dict(size=marker_size), row=0,
                      col=0,
                      selector=dict(mode='markers'))
    fig.update_layout(legend=dict(
        yanchor="bottom",
        title='Clusters',
        x=0.997,
        xanchor="right",
        y=0.041,
        font=dict(
            family="Arial",
            size=12,
            color="black"
        ),

    ))

    fig.update_xaxes(zeroline=True, zerolinewidth=1.5, zerolinecolor='black')
    fig.update_yaxes(zeroline=True, zerolinewidth=1.5, zerolinecolor='black')
    fig.show()
    fig.write_image("../../output/pca_plot.svg", engine='kaleido')


"""# Part one : Perform the clustering

## 1.   Data import

Before performing the data analysis, we need to import the data located in the file ***facilities.csv*** into a data frame.

*   Import the library **pandas** using **pd** as an alias to use its functions on the data.
*   Import the data from the file facilities.csv located in ../../output/ into a data frame variable called ***raw_data_frame***.
"""

path = f'../../input/{file_name}'

raw_data_frame = pd.read_csv(path)

"""## 2.   Data cleaning and normalization
*   Create a sub-set of the *raw_data_frame* that contains only the relevant columns for clustering: name it ***clutsering_frame***.
*   Import the class **StandardScaler**  and its method  **fit_transform** from the package **sklearn.preprocessing**
* Create an instance of the class StandardScaler that you call scaler.
*   Call the imported function **fit_transform**  to normalize the **clutsering_frame**: Assign the result to the clutsering_frame itself.

*   Create a new data frame named **normalized_frame** that contains the **clutsering_frame** as a parameter and **clutsering_frame.column** to create a new data frame of normlized data.

"""

clustering_frame = raw_data_frame[selected_clustering_variables]
clustering_frame = clustering_frame.fillna(clustering_frame.mean())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(clustering_frame)

"""## 3.   Data clustering
After importing the data, selecting the relevant columns for the clustering, and normalizing them, our facilities are ready to be clustered.
First, import the class **AgglomerativeClustering** from the module **sklearn.cluster.**

* Create a hierarchical clustering model with the paramters:
  * **affinity**='euclidean'
  * **linkage**='ward'
  * **compute_full_tree**=True
  * **n_clusters**=1

* call the model to perform the clustering using the model on the data scaled data frame **normalized_frame** by calling the function **fit_predict**.


*   Import the package **numpy** with alias **np**.
*   Calculate the number of items per cluster using the function **bincount** of the NumPy package. The result is an array that you can store in a variable called **counts_per_cluster**.
"""

# Create a hierarchical clustering model
hier_cluster_model = AgglomerativeClustering(affinity='euclidean', linkage='ward', compute_full_tree=True)
# Fit the data to the model and determine which clusters each data point belongs to:
hier_cluster_model.set_params(n_clusters=n_clusters)
clusters = hier_cluster_model.fit_predict(X_scaled)
counts_per_cluster = (np.bincount(clusters))  # count of data points in each cluster

"""After performing the cluster on the subset of the data in the data frame  **normalized_frame**, we would like to add the cluster numbers to the original data. 
Remember that you only selected specific columns from the original data set. Now it's time to see in which cluster each facility belongs.


For possible external usage, you can export the **clustered_data** to a CSV file: it should contain all the columns from the **raw_data_frame** and an extra column called cluster - it has the cluster number. 
The facilites are exported to the file **clustered_facilities**.csv under `../../output/`
"""

# Add cluster number to the original data
X_scaled_clustered = pd.DataFrame(raw_data_frame, columns=raw_data_frame.columns, index=raw_data_frame.index)
X_scaled_clustered['cluster'] = clusters
X_scaled_clustered["cluster"] = X_scaled_clustered["cluster"] + 1

X_scaled_clustered.head()
# export the data sets to csv file with cluster column
X_scaled_clustered.to_csv('../../output/clustered_facilities.csv', index=False)

"""# Part two: Visualise the clusters

After clustering our data, we would like to execute the PCA algorithm. It reduces all variables to two principial components. One of the merits: we can display the clustering results as a 2D plot.

* Show the clustering dendogram.
* Import the **PCA** class from the package **sklearn.decomposition **.
* Create a PCA model called **pca_cluserting** with *n_components=2.*
* Call the method **fit()** from the *pca_cluserting* to make the data frame fit into a model with only 2 components.
*   Call the method **transform()** from the *pca_cluserting* to transform the scaled data to the new PCA space.
* Dispaly the number of facilities per cluster.
"""

sample = clustering_frame
Z = linkage(clustering_frame, 'ward')
names = raw_data_frame['FACILITY_ID'].values
plot_dendrogram(Z, names, figsize=(20, 20))

# Create a PCA model to reduce our data to 2 dimensions for visualisation purposes 
pca_cluserting = PCA(n_components=2)
pca_cluserting.fit(X_scaled)

# Transfor the scaled data to the new PCA space
X_reduced = pca_cluserting.transform(X_scaled)

display_factorial_planes(X_reduced, 2, pca_cluserting, [(0, 1)], illustrative_var=clusters, alpha=0.9)

#  print the  number of facilites per cluster 
dict_clust = dict(enumerate(counts_per_cluster.flatten(), 0))
for c in dict_clust:
    print('\ncluster {0} : {1} facilities.\n'.format(c + 1, dict_clust.get(c)))
