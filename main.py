from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.son import SON
import init
import update
import time

def main():
    mdp = input("Entrez le mdp:\n")
    client = MongoClient("mongodb+srv://Molia:" + mdp + "@cluster0.dx5zp1v.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.vls

    #Initialization
    init.init(db)

    #Update
    while True:
        update.update(db)
        time.sleep(10)

if __name__ == "__main__":
    main()