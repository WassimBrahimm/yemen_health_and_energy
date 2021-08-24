import numpy as np
import geopy.distance


def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


lat1 = 52.515721
lon1 = 13.074462
lat2 = 52.51239291542733
lon2 = 13.108666840339081

# distance = haversine_distance(lat1, lon1, lat2, lon2)
coordinates_1 = [52.31510234355598, 12.012317214478594]
coordinates_2 = [50.576207, 11.726191]
distance_1 = haversine_distance(coordinates_1[0], coordinates_1[1], lat2, lon2)
# print(distance_1)
coords_1 = (52.31510234355598, 12.012317214478594)
coords_2 = (50.576207, 11.726191)

# distance_2 =geopy.distance.vincenty(coords_1, coords_2).km