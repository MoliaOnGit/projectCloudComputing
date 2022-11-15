from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import json
import dateutil.parser
import time
import vlille
import data_lille
import data_lyon
import data_rennes
import data_paris

mdp = input("Entrez le mdp:\n")
client = MongoClient("mongodb+srv://Molia:" + mdp + "@cluster0.dx5zp1v.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.vls


vlilles = vlille.get_vlille()

vlilles_to_insert = [
    {
        '_id': elem.get('fields', {}).get('libelle'),
        'name': elem.get('fields', {}).get('nom', '').title(),
        'geometry': elem.get('geometry'),
        'size': elem.get('fields', {}).get('nbvelosdispo') + elem.get('fields', {}).get('nbplacesdispo'),
        'source': {
            'dataset': 'Lille',
            'id_ext': elem.get('fields', {}).get('libelle')
        },
        'tpe': elem.get('fields', {}).get('type', '') == 'AVEC TPE'
    }
    for elem in vlilles
]

try: 
    db.stations.insert_many(vlilles_to_insert, ordered=False)
except:
    pass

# get data
L = [data_lille.data_lille(), data_rennes.data_rennes(), data_lyon.merge_data_lyon(), data_paris.merge_data_paris()]

# update 
while True:
    for func in L:
        datas = func        
        for data in datas:
            print("updating")
            db.datas.update_one({'city': data["city"], "station_id": data["station_id"]}, { "$set": data }, upsert=True)  

    time.sleep(10)