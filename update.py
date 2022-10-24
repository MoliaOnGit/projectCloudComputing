import vlille
import dateutil.parser

def update(db):
    vlilles=vlille.get_vlille()
    datas = [
        {
            "bike_availbale": elem.get('fields', {}).get('nbvelosdispo'),
            "stand_availbale": elem.get('fields', {}).get('nbplacesdispo'),
            "date": dateutil.parser.parse(elem.get('fields', {}).get('datemiseajour')),
            "station_id": elem.get('fields', {}).get('libelle')
        }
        for elem in vlilles
    ]
    
    try:
        for data in datas:
            db.datas.update_one({'date': data["date"], "station_id": data["station_id"]}, { "$set": data }, upsert=True)
        print("Database updated")
    except Exception as e:
        print("An error occurred\n")
        print( str(e)[0:30]+"...")
        pass
