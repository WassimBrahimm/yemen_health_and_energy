import pandas as pd

path = '/Users/wassimbrahim/Desktop/Desktop/article.energy.conflict/data_cleaning/asdaew13 copy.csv'
export_path = '/Users/wassimbrahim/Desktop/Desktop/article.energy.conflict/data_cleaning/cleaned.csv'
raw_data_frame = pd.read_csv(
    path)

print(raw_data_frame.shape[0])
df_clean = raw_data_frame
#
# df_clean = df_clean[df_clean['MIN_GROUND_2015'].isnull() == False]
# df_clean = df_clean[df_clean['MIN_GROUND_2015'].isna() == False]
#
# df_clean = df_clean[df_clean['MIN_GROUND_2016'].isnull() == False]
# df_clean = df_clean[df_clean['MIN_GROUND_2016'].isna() == False]
# # df_clean=df_clean[df_clean.duplicated(['FACILITY_ID'], keep=False)]
# print(df_clean.shape[0])
# df_clean.to_csv(export_path, index=False)
# print('done')
# print(df_clean)



print(df_clean['FACILITY_TYPE'])