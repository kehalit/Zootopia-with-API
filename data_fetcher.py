import requests
import os
from dotenv import load_dotenv


#from class_zwith_Api.test import API_KEY
load_dotenv()

API_KEY = os.getenv('API_KEY')

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
