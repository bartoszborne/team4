#!/usr/bin/python3

import mapstructure as map_s
import mapvisuals as map_v
import player
import items
import gameparser


def print_commands_help():
    print("""
┌────────────────────────────┬──────────────────────────────────────────────────────────────────┐
│ COMMAND                    │ Function                                                         │
├────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ ENTER [BUILDING/ROOM NAME] │ Enter the specified building or room. (Also accepts GO command). │
│ EXIT                       │ Exit the current room (or building).                             │
│ BRIEFCASE                  │ Look at the contents of your briefcase.                          │
│ TAKE [ITEM]                │ Take an item into your briefcase.                                │
│ DROP [ITEM]                │ Take an item out of your briefcase.                              │
│ OPEN [ITEM/ELEMENT]        │ Open an item in your briefcase or interactive element in a room. │
│ CLOSE [ITEM/ELEMENT]       │ Close an item in your briefcase or interactive element in a room.│
└────────────────────────────┴──────────────────────────────────────────────────────────────────┘""")


def list_of_items(items):
    items_string = ""
    for item in items:
        items_string = items_string + item["name"] + ", "

    items_string = items_string[0:len(items_string)-2]

    return items_string


def print_room_items(room):
    if room["items"] == []:
        print("There are no items of interest here.")
    else:
        print("There is " + list_of_items(room["items"]) + " here.")


def print_inventory(items):
    print("You have " + list_of_items(items) + "in your briefcase.")
    # Add more here later.


def print_room_name(room):
    # Display room name.
    if room["name"] == "Outside":
        print("You're OUTSIDE.")
    else:
        print("You're in the %s." % (room["name"]))


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(destination):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """


    if is_valid_exit(player.current_room["exits"], destination):
        player.current_room = move(player.current_room["exits"], destination)
        print(player.current_room["name"])
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global current_room
    global inventory

    item_in_room = False

    for item in current_room["items"]:
        if item["id"] == item_id and can_take_to_inv(inventory, item):
            inventory.append(item)
            current_room["items"].remove(item)
            item_in_room = True
    
    if item_in_room == False:
        print("You cannot take that.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global current_room
    global inventory

    item_in_inv = False

    for item in inventory:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
            item_in_inv = True

    if item_in_inv == False:
        print("You cannot drop that.")
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "help":
        print_commands_help()

    elif command[0] == "briefcase":
        print_inventory()

    else:
        print("This makes no sense.")


def print_menu(room):
    # Display room name and items.
    print_room_name(room)
    print_room_items(room)

    # Read player's input
    user_input = input("» ")

    # Normalise the input
    normalised_user_input = gameparser.normalise_input(user_input)

    return normalised_user_input


def move(exits, destination):
    # Next room to go to.
    return map_s.rooms[exits[destination]]


# This is the entry point of our program.
def main():
    game_won = False

    print("Welcome to GAME NAME, here as some commands that are common throughout the game:")
    print_commands_help()
    print("""Don't worry about remembering them all, most atypical commands will be displayed in the game, 
and you can always display the above table to remind yourself by typing the command HELP.""")

    # Main game loop
    while game_won == False:
        # Display game map
        map_v.print_map(player.current_room)

        # Show the menu with possible actions and ask the player
        command = print_menu(player.current_room)

        # Execute the player's command
        execute_command(command)

        # Check if game is won.
        if False:
            game_won = True
            print("GAME WON!")


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
if __name__ == "__main__":
    main()