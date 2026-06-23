import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

    


while True:
    pokemon_name = input("Enter the name of the Pokémon (or 'exit' to quit): ").lower()

    if pokemon_name.lower() == 'exit':
        print("Goodbye!")
        break

    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"ID: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
    else:
        print("Pokémon not found. Please try again.")