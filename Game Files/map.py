from npc import *

r_police_lobby = {
    "name": "Police Lobby",

    "items": [],

    "NPCs": [police_receptionist],

    "rooms": [r_police_lobby, r_police_player, r_police_chief, r_police_victim, r_police_interrogation]

}



b_police = {

"name": "Police Station",
# might not be necesary
"rooms": [r_police_lobby, r_police_player, r_police_chief, r_police_victim, r_police_interrogation],

"default room": r_police_lobby

}


