import vrennes
import dateutil.parser

def data_rennes():
    rennes_data = vrennes.get_rennes()
    datas = [
        {
            "bike_available": elem.get('fields', {}).get('nombrevelosdisponibles'),
            "stand_available": elem.get('fields', {}).get('nombreemplacementsdisponibles'),
            "nom": elem.get('fields', {}).get('nom'),
            "station_id": elem.get('fields', {}).get('idstation'),
            "etat": elem.get('fields', {}).get('etat'),
            "lat/lon": elem.get('fields', {}).get('coordonnees'),
            "last_update": dateutil.parser.parse(elem.get('fields', {}).get('lastupdate'))
        }
        for elem in rennes_data
    ]
    return datas

print(data_rennes())