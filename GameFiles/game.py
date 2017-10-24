#!/usr/bin/python3

import os
import mapstructure as map_s
import mapvisuals as map_v
import player
import items
import gameparser


def print_commands_help():
    print("""
┌────────────────────────────┬───────────────────────────────────────────────────────────────────┐
│ COMMAND                    │ Function                                                          │
├────────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ ENTER [BUILDING/ROOM NAME] │ Enter the specified building or room. (Also accepts GO command).  │
│ EXIT                       │ Exit the current room (or building).                              │
│ BRIEFCASE                  │ Look at the contents of your briefcase.                           │
│ TAKE [ITEM]                │ Take an item into your briefcase.                                 │
│ DROP [ITEM]                │ Take an item out of your briefcase.                               │
│ OPEN [ITEM/ELEMENT]        │ Open an item in your briefcase or interactive element in a room.  │
│ CLOSE [ITEM/ELEMENT]       │ Close an item in your briefcase or interactive element in a room. │
│ TALK to [CHARACTER]        │ Talk to a character found within a room.                          │
│ END                        │ End the game.                                                     │
└────────────────────────────┴───────────────────────────────────────────────────────────────────┘""")


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
    if player.inventory == []:
        print("Your briefcase is empty. Use TAKE [ITEM] to take something into your briefcase.")
    else:
        print("You have " + list_of_items(items) + "in your briefcase.")
    # Add more here later.


def print_room_name(room):
    # Display room name.
    if room["name"] == "Outside":
        print("You're outside. Use ENTER [BUILDING NAME] to enter a building on the map.")
    else:
        print("You're in the %s." % (room["name"]))


def print_room_npcs(room):
    if len(room["npcs"]) == 0:
        return
    else:
        for key in room["npcs"]:
            print(room["npcs"][key]["name"] + " in this room. You can TALK to " + room["npcs"][key]["id"].upper())



def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def give_item(item):
    player.inventory.append(item)
    print(item["id"] + " has been added to your briefcase.")


def execute_go(destination):
    if is_valid_exit(player.current_room["exits"], destination):
        player.current_room = move(player.current_room["exits"], destination)
    else:
        print("You cannot go there.")



def execute_take(item_id):
    item_in_room = False

    for item in player.current_room["items"]:
        if item["id"] == item_id:
            player.inventory.append(item)
            player.current_room["items"].remove(item)
            item_in_room = True
            print(item["id"] + "has been added to your briefcase.")
    
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


def conversation(dictionary, npc_id):
    options_list = []
    print("\nSelect Dialogue Option Letter:\n")

    for key in sorted(dictionary):
        print(str(key).upper() + ': "' + dictionary[key][0] + '"')

    chosen_dialogue = input("\n» ")
    dialogue_choice = gameparser.normalise_input(chosen_dialogue)

    if dialogue_choice[0] == "end":
        exit()
    elif dialogue_choice[0] == "a" or dialogue_choice[0] == "b" or dialogue_choice[0] == "c":
        print("\n· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·\n")
        print(npc_id.upper() + ': "' + dictionary[dialogue_choice[0]][1] + '"')
        if type(dictionary[dialogue_choice[0]][2]) == dict:
            conversation(dictionary[dialogue_choice[0]][2], npc_id)
        elif type(dictionary[dialogue_choice[0]][2]) == list:
            give_item(dictionary[dialogue_choice[0]][2][0])
            return False
        elif dictionary[dialogue_choice[0]][2] == "end_convo":
            return False


def execute_talk(npc):
    # Janrey's Code:
    keep_talking = True
    if npc in player.current_room["npcs"]:
        while keep_talking ==True:
            keep_talking = conversation(player.current_room["npcs"][npc]["dialogue"], player.current_room["npcs"][npc]["id"])
    else:
        print("Talk to whom?")

# Bartosz Shitty code:
"""    for key in player.current_room["npcs"]:
        if key == npc:
            npc_in_room = True
            npc_value = key[npc]

    if npc_in_room == True:
        conversation(npc_value["dialogue"])"""

        
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go" or command[0] == "enter":
        if len(command) > 1:
            if len(command) > 2:
                dest_concact = command[1] + command[2]
                execute_go(dest_concact)
            elif len(command) == 2:
                execute_go(command[1])
            else:
                print("Go where?")
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
        print_inventory(player.inventory)

    elif command[0] == "end":
        ready = input("\nSave game? (Y/N)\n» ")
        shouldload = gameparser.normalise_input(ready)

        if shouldload[0] == "y" or shouldload[0] == "yes":
            player.save()
            
        exit()

    elif command[0] == "exit":
        if player.current_room != map_s.rooms["outsideoutside"]:
            player.current_room = move(player.current_room["exits"], "exit")

    elif command[0] == "talk":
        if len(command) > 1:
            if len(command) > 2:
                npc_concact = command[1] + command[2]
                execute_talk(npc_concact)
            elif len(command) == 2:
                execute_talk(command[1])
            else:
                print("Talk to whom?")

    else:
        print("This makes no sense.")


def print_menu(room):
    # Display room name and items.
    print_room_name(room)
    print_room_items(room)
    print_room_npcs(room)

    # Read player's input
    user_input = input("\n» ")

    # Normalise the input
    normalised_user_input = gameparser.normalise_input(user_input)

    return normalised_user_input


def move(exits, destination):
    # Next room to go to.
    return map_s.rooms[exits[destination]]


# This is the entry point of our program.
def main():
    game_won = False

    # Resize the console for more room (also means no scrollback, potentially more predictable player experience?)
    os.system("mode con: cols=150 lines=42") # Not sure whether this'll work on uni comps with permission restrictions.
    
    ready = input("\nLoad existing game? (Y/N)\n» ")
    shouldload = gameparser.normalise_input(ready)

    if shouldload[0] == "y" or shouldload[0] == "yes":
        player.load()
        

    print("Welcome to GAME NAME, here as some commands that are common throughout the game:") # Add typing effect here.
    print_commands_help()
    print("""\nDon't worry about remembering them all, most atypical commands will be displayed in the game, 
and you can always display the above table to remind yourself by typing the command HELP.""") # Add typing effect here.

    ready = input("\nReady to start the game? (Y/N)\n» ")
    gamestart = gameparser.normalise_input(ready)

    if gamestart[0] == "y" or gamestart[0] == "yes":

        # Main game loop
        while game_won == False:
            # Display game map
            print("\n· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·")
            map_v.print_map(player.current_room)
            print()

            # Show the menu with possible actions and ask the player
            command = print_menu(player.current_room)

            # Execute the player's command
            execute_command(command)

            # Check if game is won.
            if False:
                game_won = True
                print("GAME WON!")

    else:
        exit()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
if __name__ == "__main__":
    main()