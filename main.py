from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import init
import update
import time

mdp = input("Entrez le mdp:\n")
client = MongoClient("mongodb+srv://Molia:" + mdp + "@cluster0.dx5zp1v.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.vls

#Initialization
init.init(db)

#Update
while True:
    update.update(db)
    time.sleep(10)
