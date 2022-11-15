import vlille
import dateutil.parser

# gets data from the city json
def data_lille():
    vlilles = vlille.get_vlille()
    datas = [
        {
            "bike_available": elem.get('fields', {}).get('nbvelosdispo'),
            "stand_available": elem.get('fields', {}).get('nbplacesdispo'),
            "date": dateutil.parser.parse(elem.get('fields', {}).get('datemiseajour')),
            "station_id": elem.get('fields', {}).get('libelle'),
            "city": "Lille"
        }
        for elem in vlilles
    ]
    return datas