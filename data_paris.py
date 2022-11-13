import vparis
import dateutil.parser

def data_info_paris():
    paris_info = vparis.get_paris_info()
    paris_stats = vparis.get_paris_status()
    data = paris_info['stations'][1]['lat']
    data_info = [
        {
            "station_id": elem["station_id"],
            "capacity": elem['capacity'],
            "lattitude": elem['lat'],
            "longitude": elem['lon'],
            "name": elem['name']
        }
        for elem in paris_info['stations']
    ]
    return data_info


def data_stats_paris():
    paris_stats = vparis.get_paris_status()
    data_stats = [
        {
            "station_id": elem['station_id'],
            "bike_available": elem['num_bikes_available'],
            "stand_available": elem['num_docks_available'],
            "is_installed": elem['is_installed'],
            "is_renting": elem['is_renting'],
            "is_returning": elem["is_returning"]
        }
        for elem in paris_stats['stations']
    ]
    return data_stats

# merge the two
def merge_data_paris():
    data1 = data_info_paris()
    data2 = data_stats_paris()
    data_final = []
    for elm2 in data2:
        for elm1 in data1:
            if elm2['station_id'] == elm1['station_id']:
                data_final.append(elm1 | elm2)
                break
    return data_final

# print(merge_data_paris())
