import pandas as pd

selected_clustering_variables = [
    'FACILITY_ID',
    # 'GOV',
    # 'DISTRICT',
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
#  import the data
old_csv = pd.read_csv('students_csv.csv')
new_csv = pd.read_csv('new_csv.csv')

# select only the relevant columns for the clustering
old_csv = old_csv[selected_clustering_variables]
new_csv = new_csv[selected_clustering_variables]

# Sort the dataframes
old_csv = old_csv.sort_values('FACILITY_ID')
new_csv = new_csv.sort_values('FACILITY_ID')
# 1304008 and  1304009 are duplicate  in the new_csv dataframe
duplicateRowsDF = new_csv[new_csv.duplicated('FACILITY_ID')]
print(duplicateRowsDF)

#  apply the round for the distances
new_csv = new_csv.round()
new_csv.to_csv('new_sorted_csv.csv', index=False)
old_csv.to_csv('old_sorted_csv.csv', index=False)

print('done')
