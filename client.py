from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import update
import time

mdp = input("Entrez le mdp:\n")
client = MongoClient("mongodb+srv://Molia:" + mdp + "@cluster0.dx5zp1v.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.vls

lat = float(input("Quelle est la latitude?\n"))
long = float(input("Quelle est la longitude?\n"))

station = db.stations.find({
   "loc": {
     "$near": {
       "$geometry": {
          "type": "Point" ,
          "coordinates": [lat ,long]
       },
     }
   }
}).limit(1)[0]

#update.update(db)

data = db.datas.find({'station_id' : station['_id']})

for i in data:
  info = i

print("La station la plus proche est " + station['name'] + " , il y a " + str(info['bike_available']) + " velos disponibles et " + str(info['stand_available']) + " emplacements disponibles. Derniere mise a jour: " + time.ctime(info['date']))