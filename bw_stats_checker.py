import requests

def get_bedwars_stats(api_key, player_name):
    base_url = "https://api.hypixel.net/player"
    params = {
        'key': api_key,
        'name': player_name,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if not data['success']:
            print("Error! Reason:", data['cause'])
            return None

        player_data = data['player']
        bedwars_stats = player_data['stats']['Bedwars']

        return bedwars_stats

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None

def display_bedwars_stats(stats):
    if stats is None:
        print("Unable to fetch BedWars stats.")
        return

    print("\nBedWars Stats:")
    print("Coins: {}".format(stats.get('coins', 0)))
    print("Wins: {}".format(stats.get('wins_bedwars', 0)))
    print("Final Kills: {}".format(stats.get('final_kills_bedwars', 0)))
    print("Final Deaths: {}".format(stats.get('final_deaths_bedwars', 0)))
    print("Beds Broken: {}".format(stats.get('beds_broken_bedwars', 0)))

if __name__ == "__main__":
    # This can be replaced with your own API key as well
    api_key = 'd64ff240-30a7-4969-84f8-3fa98020ee01'
    player_name = input("Enter the Minecraft player name: ")

    bedwars_stats = get_bedwars_stats(api_key, player_name)

    display_bedwars_stats(bedwars_stats)