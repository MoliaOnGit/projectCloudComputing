import vlille

def init(db):
    vlilles = vlille.get_vlille()
    vlilles_to_insert = [
    {
        '_id': elem.get('fields', {}).get('libelle'),
        'name': elem.get('fields', {}).get('nom', '').title(),
        'geometry': elem.get('geometry'),
        'size': elem.get('fields', {}).get('nbvelosdispo') + elem.get('fields', {}).get('nbplacesdispo'),
        'source': {
            'dataset': 'Lille',
            'id_ext': elem.get('fields', {}).get('libelle')
        },
        'tpe': elem.get('fields', {}).get('type', '') == 'AVEC TPE'
    }
    for elem in vlilles
    ]

    try: 
        db.stations.insert_many(vlilles_to_insert, ordered=False)
        print("Database initialized")
    except Exception as e:
        print("An error occurred\n")
        print( str(e)[0:30]+"...")
        pass
