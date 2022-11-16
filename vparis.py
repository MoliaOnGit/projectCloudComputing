import requests
import json
 

# récupère les infos sur les stations (id, nom, lat, long, capacité)
def get_vparis_info():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("data", []).get('stations')

# récupère les infos sur le statut des stations (id, vélos dispo, places dispo, fonctionne...)
def get_vparis_status():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("data", []).get('stations')