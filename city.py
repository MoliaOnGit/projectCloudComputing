from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import re

mdp = input("Entrez le mdp:\n")
client = MongoClient("mongodb+srv://Molia:" + mdp + "@cluster0.dx5zp1v.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.vls


def search(text):
    filter={
        'name': re.compile(text)
    }

    results = db.stations.find(
    filter=filter
    )

    for i in results:
        print("J'ai trouvé " + i['name'] + " à " + i['ville'])
        return i

def update():
    station = input("Quelle station voulez vous mettre a jour.\n")
    station = search(station)
    print(station)
    print("\nStation: " + station['name'])
    name = input("Quel nom?\n")
    size = int(input("Quelle taille?"))
    db.stations.update_one({'name' : station['name']},{"$set": {'name' : name , 'size' : size}}, upsert=True)

def delete():
    station = input("Quelle station voulez vous supprimer.\n")
    station = search(station)
    print(station)
    valid = input("Validation : Y/[n]?\n")
    if valid == "Y":
        db.stations.delete_one({'name' : station['name']})
        print("Supprimée")

def desactivate():
    lat = ("Quelle latitude?\n")
    long = ("Quelle longitude?\n")
    distance = ("Quelle rayon?\n")
    station = db.stations.find({
    "loc": {
        "$near": {
        "$geometry": {
            "type": "Point" ,
            "coordinates": [lat ,long]
        },
        
        },
        "maxDistance" : distance,
    }
    })

    for i in station:
        print("Station :" + i['Name'])
    valid = input("Validation : Y/[n]?\n")
    if valid == "Y":
        for i in station:
            db.stations.update_one({'_id' : i['_id']},{'$set': {'status' : "desactivated"}})

search("foch")
#delete()
#update()
#desactivate()