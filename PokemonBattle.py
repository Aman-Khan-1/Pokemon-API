import requests
import time

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
        StorageNumber = 0
    else:
        Attacker = Pokemon2_STATS
        Defender = Pokemon1_STATS
        StorageNumber = 1
    
    print (f"ATTACKER ISSSSS: {Attacker['name']}")
    print (f"DEFENDER ISSSSS: {Defender['name']}")

    Round_number = 1
    while True:

        print(f"ROUND {Round_number}")
        time.sleep(2)
        print(f"{Attacker['name']} attacks!!!")
        time.sleep(1)
        print("")
        Attacker_Damage = calculate_damage(Attacker, Defender)
        print(Attacker_Damage)
        Defender_HP = Defender['hp'] - Attacker_Damage
        print(f"{Defender['name']} has taken {Attacker_Damage} damage")
        if Defender_HP > 0:
            if StorageNumber == 0:
                Defender.update({Pokemon2_hp_key: Defender_HP})
            elif StorageNumber == 1:
                Defender.update({Pokemon1_hp_key: Defender_HP})
            print(f"{Defender['name']} IS STILL SURVIVING WITH {Defender['hp']} hp")
            time.sleep(2)
            print(f"NOW {Defender['name']} attacks for revenge")
            time.sleep(2)
            Defender_Damage = calculate_damage(Defender, Attacker)
            Attacker_HP = Attacker['hp'] - Defender_Damage
            print(f"{Attacker['name']} has taken {Defender_Damage} damage")
            time.sleep(3)
            if Attacker_HP > 0:
                if StorageNumber == 0:
                    Attacker.update({Pokemon1_hp_key: Attacker_HP})
                elif StorageNumber == 1:
                    Attacker.update({Pokemon2_hp_key: Attacker_HP})
                print(f"{Attacker['name']} IS ALIVE WITH {Attacker_HP} hp. He says 'COME AT ME' ")
                Round_number = Round_number + 1
                print("")
            else:
                print(f"{Attacker['name']} has fainted OH NOOO")
                print(f"{Defender['name']} is victorious with {Defender_HP} hp remaining")
                break      
        else:
            print(f"{Defender['name']} has fainted OH NOOO")
            print(f"{Attacker['name']} is victorious with {Attacker_HP} hp remaining")
            break





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
    simulate_battle("pidgey", "rattata")

"""
Helper Info:
- Use calculate_damage() for proper battle mechanics
- Remember to handle API response errors
- Keep battle display clear and informative
"""










