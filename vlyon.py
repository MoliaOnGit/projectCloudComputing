import requests
import json

# 

def get_vlyon_info():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_information.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("data", [])

def get_vlyon_status():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_status.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("data", [])