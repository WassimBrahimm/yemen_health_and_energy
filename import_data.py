import logging
from os.path import join

import pandas as pd

from functions import haversine_distance

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
#  combine for every conflict's
for index, facility in facilities_data.iterrows():
    for index_1, conflict in conflicts_data.iterrows():
        row_result = {}
        row_result['facility_id'] = facility['HF_Code']
        row_result['conflict_id'] = conflict['conflict_id']
        row_result['facility_latitude'] = facility['latitude']
        row_result['facility_longitude'] = facility['longitude']
        row_result['distance'] = haversine_distance(facility['latitude'], facility['longitude'],
                                                    conflict['latitude'], conflict['longitude'])
        rows_list.append(row_result)
result = pd.DataFrame(rows_list)
result.to_csv(join(base_path, 'test_me.csv'), sep=';',index=False)
