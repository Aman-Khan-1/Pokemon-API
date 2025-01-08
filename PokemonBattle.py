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



def simulate_battle(pokemon1, pokemon2):
    Pokemon1_pokemon_info = get_pokemon_info(pokemon1)
    Pokemon2_pokemon_info = get_pokemon_info(pokemon2)

    print(f"{pokemon1 } stats:")

    Pokemon1_Base_attack = calculate_attack(Pokemon1_pokemon_info)
    print(f"Base Attack: {Pokemon1_Base_attack}")
    Pokemon1_Base_defense = calculate_defense(Pokemon1_pokemon_info)
    print(f"Base Defense: {Pokemon1_Base_defense}")
    Pokemon1_Base_speed = calculate_speed(Pokemon1_pokemon_info)
    print(f"Base Speed: {Pokemon1_Base_speed}")
    Pokemon1_Base_hp = calculate_HP(Pokemon1_pokemon_info)
    print(f"Base HP: {Pokemon1_Base_hp}")

    print("")

    print(f"{pokemon1} calculated stats at level 50")

    Pokemon1_attack = calculate_stat(Pokemon1_Base_attack)
    print(f"Attack: {Pokemon1_attack}")
    Pokemon1_defense = calculate_stat(Pokemon1_Base_defense)
    print(f"Defense: {Pokemon1_defense}")
    Pokemon1_speed = calculate_stat(Pokemon1_Base_speed)
    print(f"Speed: {Pokemon1_speed}")
    Pokemon1_hp = calculate_hp(Pokemon1_Base_hp)
    print(f"HP: {Pokemon1_hp}")

    Pokemon1_name_key = "name"
    Pokemon1_attack_key = "attack"
    Pokemon1_defense_key = "defense"
    Pokemon1_speed_key = "speed"
    Pokemon1_hp_key = "hp"

    Pokemon1_STATS = {Pokemon1_name_key: pokemon1, Pokemon1_attack_key: Pokemon1_attack, Pokemon1_defense_key: Pokemon1_defense, Pokemon1_speed_key: Pokemon1_speed, Pokemon1_hp_key: Pokemon1_hp}
    print(Pokemon1_STATS)
    print(Pokemon1_STATS['attack'])
    

    print("")
    print(f"{pokemon2 } stats:")

    Pokemon2_Base_attack = calculate_attack(Pokemon2_pokemon_info)
    print(f"Attack: {Pokemon2_Base_attack}")
    Pokemon2_Base_defense = calculate_defense(Pokemon2_pokemon_info)
    print(f"Defense: {Pokemon2_Base_defense}")
    Pokemon2_Base_speed = calculate_speed(Pokemon2_pokemon_info)
    print(f"Speed: {Pokemon2_Base_speed}")
    Pokemon2_Base_hp = calculate_HP(Pokemon2_pokemon_info)
    print(f"HP: {Pokemon2_Base_hp}")

    print
    print(f"{pokemon2} calculated stats at level 50")

    Pokemon2_attack = calculate_stat(Pokemon2_Base_attack)
    print(f"Attack: {Pokemon2_attack}")
    Pokemon2_defense = calculate_stat(Pokemon2_Base_defense)
    print(f"Defense: {Pokemon2_defense}")
    Pokemon2_speed = calculate_stat(Pokemon2_Base_speed)
    print(f"Speed: {Pokemon2_speed}")
    Pokemon2_hp = calculate_hp(Pokemon2_Base_hp)
    print(f"HP: {Pokemon2_hp}")

    Pokemon2_name_key = "name"
    Pokemon2_attack_key = "attack"
    Pokemon2_defense_key = "defense"
    Pokemon2_speed_key = "speed"
    Pokemon2_hp_key = "hp"

    Pokemon2_STATS = {Pokemon2_name_key: pokemon2, Pokemon2_attack_key: Pokemon2_attack, Pokemon2_defense_key: Pokemon2_defense, Pokemon2_speed_key: Pokemon2_speed, Pokemon2_hp_key: Pokemon2_hp}
    print(Pokemon2_STATS)
    print(Pokemon2_STATS['attack'])

    print("")
    print(f"THE BATTLE OF THE WORLD IS COMMENCING. {pokemon1} VS {pokemon2}")
    print("OH IT IS ONNNNNNNNNNNNNN")
    print("3!!!")
    print("2!!")
    print("1!")
    print("FIGHT! A...O.. amina'maaaa")

    if Pokemon1_STATS['speed'] > Pokemon2_STATS['speed']:
        Attacker = Pokemon1_STATS
        Defender = Pokemon2_STATS
    else:
        Attacker = Pokemon2_STATS
        Defender = Pokemon1_STATS
    
    print (f"ATTACKER ISSSSS: {Attacker['name']}")
    print (f"DEFENDER ISSSSS: {Defender['name']}")

    x = 0
    while x==0:
        for i in range (0,99):
            if i == 3:
                x==1
    
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









"""
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

"""
