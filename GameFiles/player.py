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
    if not stages_completed[stage]:
        stages_completed[stage] = true
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



def unlock_hospital():
    map_s.hospital_visible = True


# Add stages here
stages_completed = {
    "First Kirill": False
}

# Add functions here
on_complete_functions = {
    "First Kirill": unlock_hospital
}
