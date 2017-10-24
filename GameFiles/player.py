import items
import mapstructure as map_s
import pickle

inventory = [items.assignment]

# Start game at the reception
current_room = map_s.rooms["outsideoutside"]

def save():
    """ Saves the game state """
    pickle.dump({"inventory": inventory, "current_room": current_room}, open("gamedata.p", "wb"))

def load():
    """ Loads the game state """
    global inventory
    global current_room
    try:
        pic = pickle.load(open("gamedata.p", "rb"))
        inventory = pic["inventory"]
        current_room = pic["current_room"]
    except FileNotFoundError:
        print("\nGame data not found! Starting from the beginning.\n")