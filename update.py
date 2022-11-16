import veloLille,veloLyon,veloParis,veloRennes

def update(db):
    datas = []
    datas.append(veloLille.update())
    datas.append(veloLyon.update())
    datas.append(veloParis.update())
    datas.append(veloRennes.update())


    try:
        for i in datas:
            for data in i:
                db.datas.update_one( {'date': data["date"], "station_id": data["station_id"]}, { "$set": data }, upsert=True)
        print("Database updated")
    except Exception as e:
        print("An error occurred\n")
        print( str(e))#[0:30]+"...")
        pass
