import vlyon
import dateutil.parser

# gets data from the city jsons

def data_info_lyon():
    lyon_info = vlyon.get_vlyon_info()
    lyon_stats = vlyon.get_vlyon_status()
    data = lyon_info['stations'][1]['lat']
    data_info = [
        {
            "station_id": elem["station_id"],
            "capacity": elem['capacity'],
            "lattitude": elem['lat'],
            "longitude": elem['lon'],
            "name": elem['name'],
            "city": "Lyon"
        }
        for elem in lyon_info['stations']
    ]
    return data_info


def data_stats_lyon():
    lyon_stats = vlyon.get_vlyon_status()
    data_stats = [
        {
            "station_id": elem['station_id'],
            "bike_available": elem['num_bikes_available'],
            "stand_available": elem['num_docks_available'],
            "is_installed": elem['is_installed'],
            "is_renting": elem['is_renting'],
            "is_returning": elem["is_returning"]
        }
        for elem in lyon_stats['stations']
    ]
    return data_stats

# merge the two
def merge_data_lyon():
    data1 = data_info_lyon()
    data2 = data_stats_lyon()
    data_final = []
    for elm2 in data2:
        for elm1 in data1:
            if elm2['station_id'] == elm1['station_id']:
                data_final.append(elm1 | elm2)
                break
    return data_final

# print(merge_data_lyon())
