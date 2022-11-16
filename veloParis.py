import vparis,time,CONST

def update():
    vpariss=vparis.get_vparis_status()
    datas = [
        {
            "bike_available": int(elem.get('num_bikes_available')),
            "stand_available": int(elem.get('num_docks_available')),
            "date": time.time(),
            "station_id": int(elem.get('station_id')) + CONST.__OFFSETPARIS__
        }
        for elem in vpariss
    ]
    return datas