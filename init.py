import stationsLille,stationsLyon,stationsParis,stationsRennes
from pymongo import GEOSPHERE

def init(db):

    db.stations.create_index([("loc",GEOSPHERE)])
    stations = []
    stations.append(stationsLille.init())
    stations.append(stationsLyon.init())
    stations.append(stationsParis.init())
    stations.append(stationsRennes.init())

    try: 
        for i in stations:
            db.stations.insert_many(i, ordered=False)
        print("Database initialized")
    except Exception as e:
        print("An error occurred during init\n")
        print(str(e))
        pass