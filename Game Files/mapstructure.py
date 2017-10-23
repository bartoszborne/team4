import npc
import items


police_visible = True
hospital_visible = True
shipping_visible = True
victim_visible = True


#---------Poloce-Station-Rooms-------------
r_police_lobby = {
    "name": "Police Lobby",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "myoffice": "myoffice", "chiefsoffice": "chiefsoffice",
    "victimsoffice": "victimsoffice", "interrogationroom": "interrogationroom"}
}

r_police_player = {
    "name": "My Office",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"exit": "policelobby", "policelobby": "policelobby"}
}

r_police_chief = {
    "name": "Chief's Office",
    "building": "Police Station",
    "items": [items.assignment],
    "npcs": [],
    "exits": {"exit": "policelobby", "policelobby": "policelobby"}
}

r_police_victim = {
    "name": "Victim's Office",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"exit": "policelobby", "policelobby": "policelobby"}
}

r_police_interrogation = {
    "name": "Interrogation Room",
    "building": "Police Station",
    "items": [],
    "npcs": [],
    "exits": {"exit": "policelobby", "policelobby": "policelobby"}
}

#-----------Outside-Room--------------

r_outside_outside = {
    "name": "Outside",
    "building": "Outside",
    "items": [],
    "npcs": [],
    "exits": {"policestation": "policelobby", "police": "policelobby"}
}

#---------ROOMS DICT-----------------
rooms = {
    "outsideoutside": r_outside_outside,
    "policelobby": r_police_lobby,
    "myoffice": r_police_player,
    "chiefsoffice": r_police_chief,
    "victimsoffice": r_police_victim,
    "interrogationroom": r_police_interrogation
}