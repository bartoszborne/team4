#!/usr/bin/python3

import os
import mapstructure as map_s
import mapvisuals as map_v
import player
import items
import gameparser
import sys
from time import sleep

godmode = False

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
│ TALK to [CHARACTER]        │ Talk to a character found within a room.                          │
│ END                        │ End the game.                                                     │
└────────────────────────────┴───────────────────────────────────────────────────────────────────┘""")


def typing_print(text):
    # Reference: https://stackoverflow.com/questions/20302331/typing-effect-in-python (Accessed: 24/10/17)
    for char in text:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    # End of Referenced material


def list_of_items(items):
    items_string = ""
    for item in items:
        items_string = items_string + item["name"] + ", "

    items_string = items_string[0:len(items_string)-2]

    return items_string


def print_room_items(room):
    if room["items"] == []:
        typing_print("There are no items of interest here.\n")
    else:
        typing_print("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory(items):
    if player.inventory != []:
        typing_print("\nYou have the following items in your in your briefcase:")
        for item in player.inventory:
            typing_print("\n· " + item["id"])
        typing_print("\n\nUse OPEN [ITEM] to view the contents of an item, if applicable.\nUse DROP [ITEM] to remove an item from your briefcase.\nPress -enter- to return.")
        response = input("\n» ")
        return response
    else:
        typing_print("\nYour briefcase is empty. Use TAKE [ITEM] to take something into your briefcase.")
        sleep(2)


def print_room_name(room):
    if room["name"] == "Outside":
        typing_print("You're outside. Use ENTER [BUILDING NAME] to enter a building on the map.\n")
    else:
        typing_print("You're in %s.\n" % (room["name"]))


def print_room_npcs(room):
    if len(room["npcs"]) == 0:
        return
    else:
        for key in room["npcs"]:
            typing_print(room["npcs"][key]["name"] + " in this room. You can TALK to " + room["npcs"][key]["id"].upper() + "\n")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def give_item(item):
    player.inventory.append(item)
    typing_print(item["id"] + " has been added to your briefcase. Use BRIEFCASE to look inside your briefcase.\n")



def execute_go(destination):
    if is_valid_exit(player.current_room["exits"], destination):
        player.current_room = move(player.current_room["exits"], destination)
    else:
        print("You cannot go there.")
        sleep(1)


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
    item_in_inv = False

    for item in player.inventory:
        if item["id"] == item_id:
            player.current_room["items"].append(item)
            player.inventory.remove(item)
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
        typing_print("YOU" + ': "' + dictionary[dialogue_choice[0]][0] + '"\n')
        sleep(1)
        typing_print(npc_id.upper() + ': "' + dictionary[dialogue_choice[0]][1] + '"\n')
        sleep(2)
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
        sleep(2)

    # (Bartosz deleted his code of shame)

def execute_open(item):
    if item["contents"] != "":
        typing_print(item["contents"])
    else:
        typing_print("This item cannot be opened.")
        sleep(2)

        
def execute_command(command):
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
                sleep(2)
        else:
            print("Go where?")
            sleep(2)

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            sleep(2)

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            sleep(2)

    elif command[0] == "help":
        print_commands_help()
        sleep(2)

    elif command[0] == "briefcase":
        inv_response = print_inventory(player.inventory)
        if inv_response == "":
            main()
        else:
            execute_command(gameparser.normalise_input(inv_response))

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
                sleep(2)

    elif command[0] == "open":
        if len(command) > 1:
            execute_open(command[1])
        else:
            print("Open what?")
            sleep(2)

    elif command[0] == "bartoszisgod":
        global godmode
        godmode = True

    else:
        print("This makes no sense.")
        sleep(2)


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


def main():
    game_won = False
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
            global godmode
            if godmode:
                game_won = True
                typing_print("\nYou've reached the end of the game. Thanks for playing\n")
                sleep(1)
                typing_print("\nCredits:\n\nTEAM 4\n\nBartosz Borne\nJanrey Mosuela\nSuraj Patel\nJoe Lewis\nLuke Atkins\nStanislav Kataev\nNour Snx\nMiltos Zoumekas\n")


# This is the entry point of our program.
def game_start():
    # Resize the console for more room (also means no scrollback, potentially more predictable player experience?)
    os.system("mode con: cols=150 lines=42")
    
    ready = input("\nLoad existing game? (Y/N)\n» ")
    shouldload = gameparser.normalise_input(ready)

    if len(shouldload) > 0:
        if shouldload[0] == "y" or shouldload[0] == "yes":
            player.load()
    else:
        game_start()          

    typing_print("\nWelcome to CSI: CARDIFF.\n\nHere as some commands that are common throughout the game:")
    print_commands_help()
    typing_print("""\nDon't worry about remembering them all, most commands will be displayed at appropiate times in the game, 
and you can always display the above table to remind yourself by typing the command HELP.""")

    ready = input("\n\nReady to start the game? (Y/N)\n» ")
    gamestart = gameparser.normalise_input(ready)

    if len(gamestart) > 0:
        if gamestart[0] == "y" or gamestart[0] == "yes":
            # Main game loop
            main()
        else:
            exit()
    else:
        game_start()


# Are we being run as a script? If so, run game_start().
# '__main__' is the name of the scope in which top-level code executes.
if __name__ == "__main__":
    game_start()