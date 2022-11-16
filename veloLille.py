import vlille,time,CONST

def update():
    vlilles=vlille.get_vlille()
    datas = [
        {
            "bike_available": int(elem.get('fields', {}).get('nbvelosdispo')),
            "stand_available": int(elem.get('fields', {}).get('nbplacesdispo')),
            "date": time.time(),
            "station_id": int(elem.get('fields', {}).get('libelle')) + CONST.__OFFSETLILLE__,
        }
        for elem in vlilles
    ]

    return datas