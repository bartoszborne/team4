import items
import mapstructure as map_s
import pickle
import npc
import dialogues


# Start game at the reception
current_room = map_s.rooms["outsideoutside"]

inventory = []

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


def get_task():
    items.task["opened"] = False

def get_assignment():
    map_s.hospital_visible = True
    map_s.rooms["hospitalreception"]["unlocked"] = True

def open_assignment():
    items.assignment["opened"] = True
    map_s.victim_visible = True
    map_s.rooms["joelivingroom"]["unlocked"] = True

def unlock_joeoffice():
    map_s.rooms["joehomeoffice"]["unlocked"] = True


def open_joefiles():
    items.joe_files["opened"] = True
    map_s.shipping_visible = True
    map_s.rooms["hospitalpatient"]["npcs"]["killer"] = npc.killer
    del(map_s.rooms["hospitalpatient"]["npcs"]["doctor"])
    items.sms["opened"] = True

def get_knife():
    map_s.rooms["policeinterrogation"]["npcs"]["killer"] = npc.killer
    if "killer" in map_s.rooms["hospitalpatient"]["npcs"]:
        del(map_s.rooms["hospitalpatient"]["npcs"]["killer"])

def get_warehousepasscode():
    map_s.rooms["shippingoffice"]["npcs"]["chief"] = npc.chief_kirill
    del(map_s.rooms["policechief"]["npcs"]["chief"])
    npc.chief_kirill["dialogue"] = dialogues.d_chief_kirill_ending
    map_s.rooms["policejail"]["npcs"]["killer"] = npc.killer
    if "killer" in map_s.rooms["policeinterrogation"]["npcs"]:
        del(map_s.rooms["policeinterrogation"]["npcs"]["killer"])

def sms_read():
    items.sms["opened"] = False


# Add stages here
stages_completed = {
    "zero": False,
    "one": False,
    "two": False,
    "three": False,
    "four": False,
    "five": False,
    "six": False,
    "smsread": False
}

# Add functions here
on_complete_functions = {
    "zero": get_task,
    "one": get_assignment,
    "two": open_assignment,
    "three": unlock_joeoffice,
    "four": open_joefiles,
    "five": get_knife,
    "six": get_warehousepasscode,
    "smsread": sms_read
}
