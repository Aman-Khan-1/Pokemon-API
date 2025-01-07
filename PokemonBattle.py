import requests

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)


def calculate_attack(information):
    BASE_STATS = information["stats"]
    for j in BASE_STATS:   
        if j['stat']['name'] == "attack":
            return (j['base_stat'])

def calculate_defense(information):
    BASE_STATS = information["stats"]
    for j in BASE_STATS:   
        if j['stat']['name'] == "defense":
            return (j['base_stat'])

def calculate_speed(information):
    BASE_STATS = information["stats"]
    for j in BASE_STATS:   
        if j['stat']['name'] == "speed":
            return (j['base_stat'])

def calculate_HP(information):
    BASE_STATS = information["stats"]
    for j in BASE_STATS:   
        if j['stat']['name'] == "hp":
            return (j['base_stat'])





def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    # TODO: Fetch Pokémon Data
    # - Create lowercase URLs for both Pokémon
    # - Make GET requests and check response codes
    # - Extract JSON data if successful

    # TODO: Calculate Initial Stats
    # - Use calculate_stat() for attack/defense/speed
    # - Use calculate_hp() for HP stats
    # - Store in dictionaries

    # TODO: Initialise Battle Display
    # - Show battle start message
    # - Display initial HP values

    # TODO: Determine First Attacker
    # - Compare speed stats
    # - Set up attacker/defender variables
    # - Store corresponding stats

    # TODO: Battle Loop
    # - Track round numbers
    # - While both have HP > 0:
    #   - Show current round
    #   - Calculate and deal damage
    #   - Check for fainting (==< 0)
    #   - Show remaining HP
    #   - Swap roles
    #   - Increment round

    # TODO: End Battle
    # - Show victory message
    # - Display winner

if __name__ == "__main__":
    simulate_battle("pikachu", "bulbasaur")

"""
Helper Info:
- Use calculate_damage() for proper battle mechanics
- Remember to handle API response errors
- Keep battle display clear and informative
"""


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url= f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return (pokemon_data)
    else:
        print(f"Failed to retrieve data {response.status_code}")

Pokemon1 = "pikachu"
Pikachu_pokemon_info = get_pokemon_info(Pokemon1)
Pokemon2 = "bulbasaur"
Bulbasaur_pokemon_info = get_pokemon_info(Pokemon2)


if Bulbasaur_pokemon_info:
    print(f"{Bulbasaur_pokemon_info["name"]}")
    print(f"{Bulbasaur_pokemon_info["id"]}")

print("Bulbasaur stats:")

Bul_Base_attack = calculate_attack(Bulbasaur_pokemon_info)
print(f"Attack: {Bul_Base_attack}")
Bul_Base_defense = calculate_defense(Bulbasaur_pokemon_info)
print(f"Defense: {Bul_Base_defense}")
Bul_Base_speed = calculate_speed(Bulbasaur_pokemon_info)
print(f"Speed: {Bul_Base_speed}")
Bul_Base_hp = calculate_HP(Bulbasaur_pokemon_info)
print(f"HP: {Bul_Base_hp}")

print("")
print("Bulbasaur calculated stats at level 50")

Bul_attack = calculate_stat(Bul_Base_attack)
print(f"Base Attack: {Bul_attack}")
Bul_defense = calculate_stat(Bul_Base_defense)
print(f"Base Defense: {Bul_defense}")
Bul_speed = calculate_stat(Bul_Base_speed)
print(f"Base Speed: {Bul_speed}")

print("")
print("Pikachu base stats:")

Pi_Base_attack = calculate_attack(Pikachu_pokemon_info)
print(f"Attack: {Pi_Base_attack}")
Pi_Base_defense = calculate_defense(Pikachu_pokemon_info)
print(f"Defense: {Pi_Base_defense}")
Pi_Base_speed = calculate_speed(Pikachu_pokemon_info)
print(f"Speed: {Pi_Base_speed}")
Pi_Base_hp = calculate_HP(Pikachu_pokemon_info)
print(f"HP: {Pi_Base_hp}")

print("")
print("Pikachu calculated stats at level 50")

Pi_attack = calculate_stat(Pi_Base_attack)
print(f"Base Attack: {Pi_attack}")
Pi_defense = calculate_stat(Pi_Base_defense)
print(f"Base Defense: {Pi_defense}")
Pi_speed = calculate_stat(Pi_Base_speed)
print(f"Base Speed: {Pi_speed}")
