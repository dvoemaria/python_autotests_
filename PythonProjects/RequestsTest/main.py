import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd0e59200cd71755e85b598dcf8e35b77'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
BODY_CREATE_POKEMONS = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE_POKEMONS)
print(response_create.text)

pokemon_id = response_create.json()['id']

'''BODY_CHANGE = {
    "pokemon_id": pokemon_id,
    "name": "Завр",
    "photo_id": 2
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.text)'''

BODY_ADD = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD)
print(response_add_pokeball.text)