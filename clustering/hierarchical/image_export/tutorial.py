# Import standard libraries
import pandas as pd
import pandas as pd

path = '/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/notes.csv'
raw_data_frame = pd.read_csv(path, delimiter=',')



clustering_frame = raw_data_frame[[
    'Algebra', 'English'

]]


from sklearn.preprocessing import normalize

data_scaled = normalize(clustering_frame)
data_scaled = pd.DataFrame(data_scaled, columns=clustering_frame.columns)

import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(15, 7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
s="""

"""
# plt.axhline(y=0.0615, color='black', linestyle='--', label='y=0.8')
# plt.axhline(y=7.2, color='black',  linestyle='--')
plt.show()
