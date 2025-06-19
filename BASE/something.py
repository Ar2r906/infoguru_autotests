import requests
from dotenv import load_dotenv
load_dotenv('../.env')

def get_something(endpoint, headers=None, params=None):
    response = requests.get(f'{endpoint}', headers=headers, params=params)
    return response

def post_something(endpoint, headers=None, params=None, json=None):
    response = requests.post(f"{endpoint}", headers=headers, params=params, json=json)
    return response

def patch_something(endpoint, headers=None, params=None, json=None):
    response = requests.patch(f"{endpoint}", headers=headers, params=params, json=json)
    return response

def delete_something(endpoint, headers=None, params=None, json=None):
    response = requests.delete(f"{endpoint}", headers=headers, params=params, json=json)
    return response