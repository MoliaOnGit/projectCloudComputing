import vlille, CONST

def init():
    vlilles = vlille.get_vlille()
    stations = [
    {
        '_id': int(elem.get('fields', {}).get('libelle')) + CONST.__OFFSETLILLE__,
        'name': elem.get('fields', {}).get('nom', '').title(),
        'long': elem.get('geometry', {}).get('coordinates')[0],
        'lat': elem.get('geometry', {}).get('coordinates')[1],
        'size': elem.get('fields', {}).get('nbvelosdispo') + elem.get('fields', {}).get('nbplacesdispo'),
        'ville': 'lille',
    }
    for elem in vlilles
    ]

    return stations