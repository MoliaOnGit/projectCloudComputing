import vlille, CONST

def init():
    vlilles = vlille.get_vlille()
    stations = [
    {
        '_id': int(elem.get('fields', {}).get('libelle')) + CONST.__OFFSETLILLE__,
        'name': elem.get('fields', {}).get('nom', '').title(),
        'loc':elem.get('geometry'),
        'size': elem.get('fields', {}).get('nbvelosdispo') + elem.get('fields', {}).get('nbplacesdispo'),
        'ville': 'lille',
    }
    for elem in vlilles
    ]
    return stations