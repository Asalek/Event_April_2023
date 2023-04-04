import requests

# Set the base URL for the PokeAPI
BASE_URL = 'https://pokeapi.co/api/v2/'

# Prompt the user for a Pokemon name
pokemon_name = input('Enter a Pokemon name: ')

# Send an HTTP GET request to the PokeAPI to retrieve information about the Pokemon
# response = requests.get(f'{BASE_URL}pokemon/{pokemon_name}')
response = requests.get(BASE_URL + 'pokemon/' + pokemon_name)

# If the response is successful, retrieve the JSON data
	# print
if response.status_code == 200:
    pokemon_data = response.json()
    # Extract the relevant information from the JSON data
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    # Print the information
    print('%s abilities:' % name)
    print(', '.join(abilities))
else:
    print('no pokemon')
