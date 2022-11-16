import vlyon,time,CONST

def update():
    vlyons=vlyon.get_vlyon_status()
    datas = [
        {
            "bike_available": int(elem.get('num_bikes_available')),
            "stand_available": int(elem.get('num_docks_available')),
            "date": time.time(),
            "station_id": int(elem.get('station_id')) + CONST.__OFFSETLYON__
        }
        for elem in vlyons
    ]
    return datas