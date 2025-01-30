import requests
import json


API_KEY = "CdYYw0zODjWdMdm9rdeXeg==GjH45xRiPvGqfrSp"

def fetch_animals(animal_name):
    url = f'https://api.api-ninjas.com/v1/animals?X-Api-Key={API_KEY}&name={animal_name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return None
    else:
        print("Error fetching data from API")
        return None
