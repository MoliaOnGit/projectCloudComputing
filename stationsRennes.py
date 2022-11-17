import vrennes,CONST

def init():
    vrenness = vrennes.get_rennes()

    stations = [
        {
            '_id': int(elem.get('fields', {}).get('idstation')) + CONST.__OFFSETRENNES__,
            'name': elem.get('fields', {}).get('nom'),
            'loc': elem.get('geometry'),
            'size': elem.get('fields', {}).get('nombreemplacementsactuels'),
            'ville': 'rennes',
        }
        for elem in vrenness
    ]

    return stations