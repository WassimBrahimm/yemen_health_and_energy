import pandas as pd
from scipy.spatial import distance_matrix
from scipy.spatial.distance import squareform, pdist

df = pd.read_csv('/Users/wassimbrahim/Desktop/article.energy.conflict/clustering/hierarchical/csv_import/notes.csv')
ctys = list(df['student'])
# df = pd.DataFrame(data, columns=['English', 'Algebra'], index=ctys)
# print(df)
# distances = pd.DataFrame(distance_matrix(df.values, df.values), index=df['student'], columns=df.index)
sle = df[['Algebra', 'English']]
distances = pd.DataFrame(distance_matrix(sle.values, sle.values), index=df['student'], columns=df['student'])
print(distances)
distances.to_csv('distances.csv',index=False)