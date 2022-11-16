import vrennes,time,CONST

def update():
    vrenness=vrennes.get_rennes()
    datas = [
        {
            "bike_available": int(elem.get('fields', {}).get('nombrevelosdisponibles')),
            "stand_available": int(elem.get('fields', {}).get('nombreemplacementsdisponibles')),
            "date": time.time(),
            "station_id": int(elem.get('fields', {}).get('idstation')) + CONST.__OFFSETRENNES__,
        }
        for elem in vrenness
    ]
    return datas