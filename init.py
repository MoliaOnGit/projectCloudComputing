import stationsLille,stationsLyon,stationsParis,stationsRennes

def init(db):
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
        pass