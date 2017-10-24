import npc
import items


police_visible = True
hospital_visible = True
shipping_visible = True
victim_visible = True


#---------Police-Station-Rooms-------------
r_police_lobby = {
    "name": "the Police Lobby",
    "building": "Police Station",
    "items": [],
    "npcs": {}, 
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
    "name": "the Chief's Office",
    "building": "Police Station",
    "items": [items.assignment],
    "npcs": {"chief": npc.chief_kirill},
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
    "name": "the Interrogation Room",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "jailroom": "policejail"}
}


r_police_jail = {
    "name": "the Jail Room",
    "building": "Police Station",
    "items": [],
    "npcs": {},
    "exits": {"exit": "policelobby", "policelobby": "policelobby", "myoffice": "policeplayer", "chiefsoffice": "policechief",
    "joesoffice": "policejoe", "interrogationroom": "policeinterrogation"}
}

#---------Hospital-Rooms-------------
r_hospital_reception = {
    "name": "the Hospital Reception",
    "building": "Hospital",
    "items": [],
    "npcs": {"hospitalreceptionist": npc.hospital_receptionist}, #CHANGE ME LATER! you pleb!
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "patientsroom": "hospitalpatient", "joesroom": "hospitalpatient", "surveillanceroom": "hospitalsurveillance"}
}

r_hospital_patient = {
    "name": "Joe's Room",
    "building": "Hospital",
    "items": [],
    "npcs": {"joe": npc.joe_branson, "doctor": npc.doctor_kim}, # ADD THE ASIAN (DR KIM JONGUN) DOCTOR
    "exits": {"exit": "hospitalreception", "hospitalreception": "hospitalreception"}
}

r_hospital_surveillance = {
    "name": "the Surveillance Room",
    "building": "Hospital",
    "items": [],
    "npcs": {},
    "exits": {"exit": "hospitalreception", "hospitalreception": "hospitalreception"}
}

#---------Joe's House-Rooms-------------
r_joehouse_living = {
    "name": "the Living Room",
    "building": "Joe's House",
    "items": [],
    "npcs": {"mrsbranson": npc.joe_wife}, #CHANGE ME LATER! you pleb!
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "office": "joehomeoffice", "joesoffice": "joehomeoffice"}
}

r_joehouse_office = {
    "name": "Joe's Home Office",
    "building": "Joe's House",
    "items": [],
    "npcs": {}, # ADD THE ASIAN (DR KIM JONGUN) DOCTOR
    "exits": {"exit": "joelivingroom", "livingroom": "joelivingroom"}
}


#---------Shipping-Rooms-------------
r_shipping_warehouse = {
    "name": "the Shipping Warehouse",
    "building": "Shipping Company",
    "items": [],
    "npcs": {"ceo": npc.shipping_ceo}, #CHANGE ME LATER! you pleb!
    "exits": {"exit": "outsideoutside", "outside": "outsideoutside", "building": "outsideoutside", "shippingoffice" : "shippingoffice", "office" : "shippingoffice"}
}

r_shipping_office = {
    "name": "the Shipping Company's Office",
    "building": "Shipping Company",
    "items": [],
    "npcs": {}, # ADD THE ASIAN (DR KIM JONGUN) DOCTOR
    "exits": {"exit": "shippingwarehouse", "shippingwarehouse": "shippingwarehouse", "warehouse": "shippingwarehouse",}
}


#-----------Outside-Room--------------

r_outside_outside = {
    "name": "Outside",
    "building": "Outside",
    "items": [],
    "npcs": [],
    "exits": {"policestation": "policelobby", "police": "policelobby", "hospital": "hospitalreception", "shipping": "shippingwarehouse", "shippingcompany": "shippingwarehouse", "joeshouse": "joelivingroom"}
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
    #----------------Joe's House WAREHOUSE DICT-------------------|
    "joelivingroom": r_joehouse_living,
    "joehomeoffice": r_joehouse_office,
    #----------------SHIPPING WAREHOUSE DICT-------------------|
    "shippingwarehouse": r_shipping_warehouse,
    "shippingoffice": r_shipping_office,
}