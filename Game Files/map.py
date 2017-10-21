from npc import *

police_visible = True
hospital_visible = True
shipping_visible = True
victim_visible = True

def print_city_map(police_visible, hospital_visible, shipping_visible, victim_visible):
    if police_visible:
        print_police = [" Police Station ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_police = ["                ", "                ", "                "]

    if hospital_visible:
        print_hospital = ["    Hospital    ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_hospital = ["                ", "                ", "                "]

    if shipping_visible:
        print_shipping = ["Shipping Company", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_shipping = ["                ", "                ", "                "]

    if victim_visible:
        print_victim = [" Victim's House ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_victim = ["                ", "                ", "                "]
    
    city_map = """╔═════════════════════════ CITY MAP - BUILDINGS ═════════════════════════╗
║                                                ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓║
║                                                     ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓║
║     %s                                   ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓║
║     %s                                        ▒▒▒▒▒▒▒▒▓▓▓║
║     %s                                            ▒▒▒▒▒▓▓║
║                                        %s        ▒▒▒▒▒▓▓▓║
║                                        %s        ▒▒▒▒▒▒▓▓║
║                                        %s         ▒▒▒▒▒▒▓║
║                                                                     ▒▒▒║
║                                                                       ▒║
║\_                                                                      ║
║░░\                                                                     ║
║░░░|                                                                    ║
║░░/                                             %s        ║
║░|   %s                           %s        ║
║░░\  %s                           %s        ║
║░░░\_%s                                                   ║
║░░░░░\____                                                              ║
║░░░░░░░░░░\                                                             ║
╚════════════════════════════════════════════════════════════════════════╝""" % (print_hospital[0], print_hospital[1], print_hospital[2],
    print_police[0], print_police[1], print_police[2],
    print_victim[0], print_shipping[0], print_victim[1], print_shipping[1], print_victim[2], print_shipping[2])

    print(city_map)


#---------Poloce-Station-Rooms-------------
r_police_lobby = {
    "name": "Police Lobby",
    "building": "Police Station",
    "items": [],
    "npcs": [police_receptionist],
    "exits": {"building": r_outside_outside, "myoffice": r_police_player, "chiefsoffice": r_police_chief,
    "victimsoffice": r_police_victim, "interrogationroom": r_police_interrogation}
}

r_police_player = {
    "name": "My Office",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"policelobby": r_police_lobby}
}

r_police_chief = {
    "name": "Chief's Office",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"policelobby": r_police_lobby}
}

r_police_victim = {
    "name": "Victim's Office",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"policelobby": r_police_lobby}
}

r_police_interrogation = {
    "name": "Interrogation Room",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"policelobby": r_police_lobby}
}

#-----------Outside-Room--------------

r_outside_outside = {
	"name": "Outside",
	"building": "Outside",
    "items": [],
    "npcs": [],
    "exits": {"policestation": r_police_lobby}
}