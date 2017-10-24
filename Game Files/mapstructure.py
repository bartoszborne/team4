import npc
import items


police_visible = True
hospital_visible = True
shipping_visible = True
victim_visible = True


#---------Police-Station-Rooms-------------
r_police_lobby = {
    "name": "Police Lobby",
    "building": "Police Station",
    "items": [],
    "npcs": {}, #CHANGE ME LATER! you pleb!
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "interrogationroom": "policeinterrogation", "jailroom": "policejail"}
}

r_police_player = {
    "name": "My Office",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "interrogationroom": "policeinterrogation", "jailroom": "policejail"}
}

r_police_chief = {
    "name": "Chief's Office",
    "building": "Police Station",
    "items": [items.assignment],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer",
    "joesoffice": "policejoe", "interrogationroom": "policeinterrogation", "jailroom": "policejail"}
}

r_police_joe = {
    "name": "Joe's Office",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "interrogationroom": "policeinterrogation", "jailroom": "policejail"}
}

r_police_interrogation = {
    "name": "Interrogation Room",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "jailroom": "policejail"}
}


r_police_jail = {
    "name": "Jail Room",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "interrogationroom": "policeinterrogation"}
}

#---------Hospital-Rooms-------------
r_hospital_reception = {
    "name": "Hospital Reception",
    "building": "Hospital",
    "items": [],
    "npcs": {"hospitalreceptionist": npc.hospital_receptionist}, #CHANGE ME LATER! you pleb!
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "patientsroom": "patientsroom", "surveillanceroom": "surveillanceroom"}
}

r_hospital_patient = {
    "name": "Joe's Ward Room",
    "building": "Hospital",
    "items": [],
    "npcs": {"joe": npc.joe_branson},
    "exits": {"exit": "hospitalreception", "hospitalreception": "hospitalreception"}
}

r_hospital_surveillance = {
    "name": "Surveillance Room",
    "building": "Hospital",
    "items": [],
    "npcs": {},
    "exits": {"exit": "hospitalreception", "hospitalreception": "hospitalreception"}
}

#-----------Outside-Room--------------

r_outside_outside = {
    "name": "Outside",
    "building": "Outside",
    "items": [],
    "npcs": [],
    "exits": {"policestation": "policelobby", "police": "policelobby", "hospital": "hospitalreception"}
}

#---------ROOMS DICT-----------------
rooms = {
    "outsideoutside": r_outside_outside,
    #----------------------POLICE DICT-------------------|
    "policelobby": r_police_lobby,
    "policeplayer": r_police_player,
    "policechief": r_police_chief,
    "policejoe": r_police_joe,
    "policeinterrogation": r_police_interrogation,
    "policejail": r_police_jail,
    #--------------------HOSPITAL DICT-------------------|
    "hospitalreception": r_hospital_reception,
    "hospitalpatient": r_hospital_patient,
    "hospitalsurveillance": r_hospital_surveillance,
    #--------------------HOSPITAL DICT-------------------|
    "hospitalreception": r_hospital_reception,
    "hospitalpatient": r_hospital_patient,
    "hospitalsurveillance": r_hospital_surveillance,
    #--------------------OFFICE DICT-------------------|
    "hospitalreception": r_hospital_reception,
    "hospitalpatient": r_hospital_patient,
    "hospitalsurveillance": r_hospital_surveillance,
}