import logging
from os.path import join

import pandas as pd

from haversine import haversine

base_path = '/Users/wassimbrahim/Desktop/yemeni_conflict_data'
f_name = 'yemen_health_facilities.csv'
# read the health facilities  data into facilities_data
facilities_data = pd.read_csv(join(base_path, f_name), delimiter=';', skip_blank_lines=True)
logging.info('File {0} imported successfully.'.format(f_name))
facilities_data['latitude'] = 52.31510234355598
facilities_data['longitude'] = 12.012317214478594
lat2 = 52.51239291542733
lon2 = 13.108666840339081
f_name = 'conflicts.csv'
conflicts_data = pd.read_csv(join(base_path, f_name), delimiter=';', skip_blank_lines=True)
logging.info('File {0} imported successfully.'.format(f_name))

result = pd.DataFrame()
rows_list = []
#  combine for every conflict: conflict date,
# final data frame columns : FID (facility_id), CID (conflict_id), conflict_date, conflict_type, facility_type,
# f_c_distance, Governorate,District,District_Pcode, GEO9_Type, HF_Code, Name_En, Type, Level,Functionality
for index, facility in facilities_data.iterrows():
    for index_1, conflict in conflicts_data.iterrows():
        merge_row = {}
        merge_row['facility_id'] = facility['FID']
        merge_row['Governorate'] = facility['Governorate']
        merge_row['District'] = facility['District']
        merge_row['District_Pcode'] = facility['District_Pcode']
        merge_row['GEO9_Type'] = facility['GEO9_Type']
        merge_row['HF_Code'] = facility['HF_Code']
        merge_row['Name_En'] = facility['Name_En']
        merge_row['Type'] = facility['Type']
        merge_row['Level'] = facility['Level']
        merge_row['Functionality'] = facility['Functionality']
        merge_row['conflict_id'] = conflict['conflict_id']
        #  add conflict details : type
        merge_row['f_c_distance'] = haversine((facility['latitude'], facility['longitude']),
                                              (conflict['latitude'], conflict['longitude']),
                                              unit='km')
        rows_list.append(merge_row)
result = pd.DataFrame(rows_list)
result.to_csv(join(base_path, 'test_me.csv'), sep=';',index=False)
