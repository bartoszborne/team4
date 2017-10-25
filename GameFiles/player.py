import items
import mapstructure as map_s
import pickle
import npc


# Start game at the reception
current_room = map_s.rooms["outsideoutside"]

inventory = [items.assignment]

# THIS IS THE ONLY FUNCTION YOU SHOULD USE
# the rest ius done by my code
def complete_stage(stage):
    if stages_completed[stage] == False:
        stages_completed[stage] = True
        on_complete_functions[stage]()


def restore_stages(stages):
    for stage in stages:
        if stages[stage]:
            complete_stage(stage)


def save():
    """ Saves the game state """
    pickle.dump({"inventory": inventory, "current_room": current_room, "npc": npc.get_npc(), "stages_completed": stages_completed}, open("gamedata.p", "wb"))

def load():
    """ Loads the game state """
    global inventory
    global current_room
    try:
        pic = pickle.load(open("gamedata.p", "rb"))
        inventory = pic["inventory"]
        current_room = pic["current_room"]
        npc.restore_npc(pic["npc"])
        restore_stages(pic["stages_completed"])
    except FileNotFoundError:
        print("\nGame data not found! Starting from the beginning.\n")



def get_assignment():
    map_s.hospital_visible = True
    map_s.rooms["hospitalreception"]["unlocked"] = True

def open_assignment():
    items.assignment["opened"] = True
    map_s.victim_visible = True
    map_s.rooms["joelivingroom"]["unlocked"] = True

def unlock_joeoffice():
    map_s.rooms["joehomeoffice"]["unlocked"] = True
    map_s.rooms["hospitalpatient"]["npcs"]["killer"] = npc.killer
    del(map_s.rooms["hospitalpatient"]["npcs"]["doctor"])


def open_joefiles():
    items.joe_files["opened"] = True
    map_s.shipping_visible = True
    map_s.rooms["shippingwarehouse"]["unlocked"] = True


# Add stages here
stages_completed = {
    "one": False,
    "two": False,
    "three": False,
    "four": False
}

# Add functions here
on_complete_functions = {
    "one": get_assignment,
    "two": open_assignment,
    "three": unlock_joeoffice,
    "four": open_joefiles
}
