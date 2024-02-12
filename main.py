import a2s  # use https://github.com/Yepoleb/python-a2s
import requests
import json
import time
import environment
import players

server_list = {
    'THE MENTLE INSTITUTION 32 Player': ('91.216.250.55', 27015),
    'FREAK FORTRESS | NY 32 Player': ('91.216.250.54', 27015),
    '2FORT | NY 24 Player': ('91.216.250.52', 27015),
    '2FORT+ | NY 32 Player': ('91.216.250.50', 27015),
    '2FORT 100 | US 100 Player': ('91.216.250.42', 27015),
    '2FORT+ | US 32 Player': ('91.216.250.41', 27015),
    'CASUAL | US 24 Player': ('91.216.250.40', 27015),
    'SURF | US 32 Player': ('91.216.250.38', 27015),
    '2FORT | US 24 Player': ('91.216.250.37', 27015),
    'TURBINE+ | NY 32 Player': ('91.216.250.35', 27015),
    'CASUAL | NY 24 Player': ('91.216.250.34', 27015),
    'CLASS WARS | US 64 Player': ('91.216.250.33', 27015),
    "Bottigers 24/7 Idle Trade 32 Player": ('91.216.250.32', 27015),
    '2FORT+ 2| US 32 Player': ('91.216.250.31', 27015),
    'TRADE | US 64 Player': ('91.216.250.30', 27015),
    '2FORT+ | EU 32 Player': ('91.216.250.234', 27015),
    'TURBINE+ | EU 64 Player': ('91.216.250.233', 27015),
    'ZOMBIE ESCAPE | EU 64 Player': ('91.216.250.232', 27015),
    'DUSTBOWL+ | EU 32 Player': ('91.216.250.231', 27015),
    'TRADE | EU 64 Player': ('91.216.250.230', 27015),
    '2FORT | LA 24 Player': ('91.216.250.22', 27015),
    '2FORT | EU 24 Player': ('91.216.250.229', 27015),
    'DEATH RUN | EU 32 Player': ('91.216.250.228', 27015),
    '2FORT+ | EU 64 Player': ('91.216.250.227', 27015),
    'PAYLOAD+ | EU 32 Player': ('91.216.250.226', 27015),
    'TURBINE | EU 24 Player': ('91.216.250.225', 27015),
    'CLASS WARS | EU 64 Player': ('91.216.250.224', 27015),
    'CASUAL | LA 1 24 Player': ('91.216.250.21', 27015),
    '2FORT+ | LA 32 Player': ('91.216.250.20', 27015),
    '2FORT | AU 24 Player': ('91.216.250.194', 27015),
    '2FORT+ | AU 32 Player': ('91.216.250.193', 27015),
    'HARVEST | US 32 Player': ('91.216.250.18', 27015),
    'HIGHTOWER | US 32 Player': ('91.216.250.17', 27015),
    'TURBINE+ | US 64 Player': ('91.216.250.16', 27015),
    '2FORT | ASIA 24 Player': ('91.216.250.161', 27015),
    '2FORT+ | ASIA 32 Player': ('91.216.250.160', 27015),
    'ZOMBIE ESCAPE | US 64 Player': ('91.216.250.15', 27015),
    'DEATH RUN | US 32 Player': ('91.216.250.13', 27015),
    'DUSTBOWL+ | US 32 Player': ('91.216.250.12', 27015),
    'PAYLOAD+ | US 32 Player': ('91.216.250.11', 27015),
    '2FORT+ | US 1 64 Player': ('91.216.250.10', 27015),
    '2FORT | BR 24 Player': ('45.89.30.55', 27016),
    '2FORT+ | BR 32 Player': ('45.89.30.55', 27015)
}


players = players.players

# Parse your player list to get the users name and put it into a map
parsed_player_list = {}
for nickname, steam_id in players.items():
    base_url = requests.get(
        f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={environment.key}&steamids={steam_id}")
    base_url_parsed = json.loads(base_url.content)
    account_name = base_url_parsed['response']['players'][0]['personaname']
    parsed_player_list[account_name] = nickname

while True:
    for server_name, server_ip in server_list.items():
        # get the players names from their steam profile
        # print("Attempting to connect to " + server_name)
        for online_players in a2s.players(server_ip):
            if online_players.name in parsed_player_list.keys():
                print(f"{parsed_player_list[online_players.name]} detected on {server_name} at {time.ctime()} ")
    time.sleep(60)