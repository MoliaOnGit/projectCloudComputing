import vparis,CONST

def init():
    vpariss = vparis.get_vparis_info()

    stations = [
        {
            '_id': int(elem.get('station_id')) + CONST.__OFFSETPARIS__,
            'name': elem.get('name'),
            'loc':{'type': "Point", 'coordinates': [elem.get('lon'),elem.get('lat')]} ,
            'size':elem.get('capacity'),
            'ville':'paris',
        }
        for elem in vpariss
    ]

    return stations