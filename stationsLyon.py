import vlyon,CONST

def init():
    vlyons = vlyon.get_vlyon_info()

    stations = [
        {
            '_id': int(elem.get('station_id')) + CONST.__OFFSETLYON__,
            'name': elem.get('name'),
            'loc':{'type': "Point", 'coordinates': [elem.get('lon'),elem.get('lat')]} ,
            'size':elem.get('capacity'),
            'ville':'lyon',
        }
        for elem in vlyons
    ]

    return stations

init()