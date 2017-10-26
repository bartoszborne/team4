#!/usr/bin/python3

import os
import mapstructure as map_s
import mapvisuals as map_v
import player
import items
import gameparser
import sys
from time import sleep
import npc
import dialogues


game_success = False


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
    typing_print("\n\nPress -enter- to return.")
    response = input("\n» ")


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
    if chosen_exit in exits:
        if map_s.rooms[exits[chosen_exit]]["unlocked"]:
            can_go = "unlocked"
        else:
            can_go = "locked"
    else:
        can_go = "not"

    return can_go


def give_item(item):
    player.inventory.append(item)
    typing_print("\n" + item["id"] + " has been added to your briefcase. Use BRIEFCASE to look inside your briefcase.\n")
    sleep(2)


def execute_go(destination):
    if is_valid_exit(player.current_room["exits"], destination) == "unlocked":
        player.current_room = move(player.current_room["exits"], destination)
    elif is_valid_exit(player.current_room["exits"], destination) == "locked":
        typing_print("That room is locked. Use UNLOCK [ROOM NAME] to unlock the door if you have a key.\n")
        sleep(2)
    else:
        print("You cannot go there.")
        sleep(2)


def execute_take(item_id):
    item_in_room = False

    for item in player.current_room["items"]:
        item_not_concact = gameparser.normalise_input(item["id"])
        if len(item_not_concact) > 1:
            item_concact = item_not_concact[0] + item_not_concact[1]
        else:
            item_concact = item_not_concact[0]
        if item_concact == item_id:
            player.inventory.append(item)
            player.current_room["items"].remove(item)
            item_in_room = True
            typing_print("\n" + item["id"] + " has been added to your briefcase.\n")
            sleep(2)
    
    if item_in_room == False:
        print("You cannot take that.")
        sleep(2)
    

def execute_drop(item_id):
    item_in_inv = False

    for item in player.inventory:
        item_not_concact = gameparser.normalise_input(item["id"])
        if len(item_not_concact) > 1:
            item_concact = item_not_concact[0] + item_not_concact[1]
        else:
            item_concact = item_not_concact[0]
        if item_concact == item_id:
            player.current_room["items"].append(item)
            player.inventory.remove(item)
            item_in_inv = True

    if item_in_inv == False:
        print("\nYou cannot drop that.\n")
        sleep(2)


def game_failed():
    typing_print("\nYou have failed the game...\n")
    sleep(2)
    game_start()


def game_win():
    global game_success
    game_success = True


def conversation(dictionary, npc_id):
    print("\nSelect dialogue option letter or press -enter- to return:\n")

    for key in sorted(dictionary):
        print(str(key).upper() + ': "' + dictionary[key][0] + '"')

    chosen_dialogue = input("\n» ")
    if chosen_dialogue != "":

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
                dial_index = npc.npc_dict[npc_id]["d_index"]
                npc.npc_dict[npc_id]["dialogue"] = dialogues.dialswap[npc_id][dial_index]
                npc.npc_dict[npc_id]["d_index"] = dial_index + 1
                return False
            elif dictionary[dialogue_choice[0]][2] == "end_convo":
                return False
            elif dictionary[dialogue_choice[0]][2] == "end_game":
                game_failed()
            elif dictionary[dialogue_choice[0]][2] == "win_game":
                game_win()
            elif dictionary[dialogue_choice[0]][2] == "inc_convo":
                dial_index = npc.npc_dict[npc_id]["d_index"]
                npc.npc_dict[npc_id]["dialogue"] = dialogues.dialswap[npc_id][dial_index]
                npc.npc_dict[npc_id]["d_index"] = dial_index + 1
                return False
    else:
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

def execute_open(item_concact):
    if items.item_dict[item_concact] in player.inventory:
        if items.item_dict[item_concact]["contents"] != "":
            typing_print(items.item_dict[item_concact]["contents"])
            items.item_dict[item_concact]["opened"] = True
            typing_print("\n\nPress -enter- to return.")
            input("\n» ")
            execute_command(["briefcase"])

        else:
            typing_print("This item cannot be opened.")
            sleep(2)
            execute_command(["briefcase"])
    else:
            typing_print("This item cannot be opened.")
            sleep(2)
            execute_command(["briefcase"])

def execute_unlock(destination):
    if is_valid_exit(player.current_room["exits"], destination) == "unlocked" or is_valid_exit(player.current_room["exits"], destination) == "locked":
        room_to_unlock = move(player.current_room["exits"], destination)
        if room_to_unlock == map_s.rooms["joehomeoffice"]:
            if items.joe_keys in player.inventory:
                room_to_unlock["unlocked"] = True
            else:
                print("You dont have an item to unlock this room.")

        if room_to_unlock == map_s.rooms["shippingwarehouse"]:
            if items.warehouse_passcode in player.inventory:
                room_to_unlock["unlocked"] = True
            else:
                print("You dont have an item to unlock this room.")

    else:
        print("You cannot unlock that. Incorrect room name or room out of reach.")
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
            if len(command) > 2:
                take_concact = command[1] + command[2]
                execute_take(take_concact)
            elif len(command) == 2:
                execute_take(command[1])
            else:
                print("Take what?")
                sleep(2)
        else:
            print("Take what?")
            sleep(2)

    elif command[0] == "drop":
        if len(command) > 1:
            if len(command) > 2:
                drop_concact = command[1] + command[2]
                execute_drop(drop_concact)
            elif len(command) == 2:
                execute_drop(command[1])
            else:
                print("Drop what?")
                sleep(2)
        else:
            print("Drop what?")
            sleep(2)

    elif command[0] == "help":
        help_response = print_commands_help()
        if help_response == "":
            main()

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

    elif command[0] == "save":
        player.save()

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
            if len(command) > 2:
                open_concact = command[1] + command[2]
                execute_open(open_concact)
            elif len(command) == 2:
                execute_open(command[1])
            else:
                print("Open what?")
                sleep(2)
        else:
            print("Open what?")
            sleep(2)

    elif command[0] == "unlock":
        if len(command) > 1:
            if len(command) > 2:
                dest_concact = command[1] + command[2]
                execute_unlock(dest_concact)
            elif len(command) == 2:
                execute_unlock(command[1])
            else:
                print("Unlock where?")
                sleep(2)
        else:
            print("Unlock where?")
            sleep(2)

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

            # Check stages and trigger stages
            if items.assignment in player.inventory:
                player.complete_stage("one")

            if items.assignment["opened"]:
                player.complete_stage("two")

            if map_s.rooms["joehomeoffice"]["unlocked"] == True:
                player.complete_stage("three")

            if items.joe_files["opened"]:
                player.complete_stage("four")

            if items.knife in player.inventory:
                player.complete_stage("five")

            if items.warehouse_passcode in player.inventory:
                player.complete_stage("six")

            if items.sms["opened"]:
                typing_print("\nTEXT MESSAGE FROM HOSPITAL:\nThe patient Joe Branson is has regained consciousness. Please come to the hospital.")
                sleep(5)

            # Check if game is won.
            if game_success:
                game_won = True
                typing_print("\nYou've reached the end of the game. Thanks for playing\n")
                sleep(1)
                typing_print("\nCredits:\n\nTEAM 4\n\nBartosz Borne\nJanrey Mosuela\nSuraj Patel\nJoe Lewis\nLuke Atkins\nStanislav Kataev\nNour Snx\nMiltos Zoumekas\n")

            # Display game map
            print("\n· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·")
            map_v.print_map(player.current_room)
            print()

            # Show the menu with possible actions and ask the player
            command = print_menu(player.current_room)

            # Execute the player's command
            execute_command(command)



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

    typing_print("\nWelcome to CSI: CARDIFF.\n\nMost commands will be displayed at appropiate times in the game, but you can always display the game commands by typing the command HELP.")

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