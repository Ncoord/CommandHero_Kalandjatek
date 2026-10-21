
# --------------------------- IMPORTING THE MAIN MODULS ---------------------------

import os
import shutil
from random import randint
from functions import *
from descriptions import *
from variables import *
from items import *
from cases import *
import subprocess

# ----------------------------- CLEARING THE TERMINAL -----------------------------

cmd(c)      # set the terminals color scheme
clear()     # and clear the terminal

# ----------------- START PLAYING MUSIC WHEN ENTERING CMD ------------------

if not playing_music:
    played_music = subprocess.Popen(["python", "music.py", r"music\loophero_loopblues.wav", str(int(True))])
    playing_music = True

# ----------------------------- SETTING UP THE PLAYER -----------------------------

while asking: # Get the player's name and class
    # -----------------------------------------------------------------------------
    while True: # Set player's name
        print_center(f'''
{"\n"*3}
{read_txt(r"ascii\title.txt")}

{text[title]}


        
{eventDescription[greeting]}
{eventDescription[what_is_name]}
''')
        player["name"] = input("\n> ")
        clear()

        if player["name"] != "": break
        else:
            print_center(f'''
{read_txt(r"ascii\void.txt")}
{c1}{text[invalid_name]}



{text[try_again]}{r}{c}''')
            input("\n> ")
            clear()

    # -----------------------------------------------------------------------------
    while True: # Draw a screen for choosing a class
        print_center(f'''
{c3}{b}[{text[soldier_title]}]{bff}
{read_txt(r"ascii\soldier.txt")}
{eventDescription[soldier_class]}{r}

{c6}{b}[{text[mage_title]}]{bff}
{read_txt(r"ascii\mage.txt")}
{eventDescription[mage_class]}{r}

{c2}{b}[{text[thief_title]}]{bff}
{read_txt(r"ascii\thief.txt")}
{eventDescription[thief_class]}{r}




{text[choose_class]}

{c3}(1){r} The Honorable Path of Soldiers
{c6}(2){r} Mysterious Beings — The Magicians
{c2}(3){r} The Thieves' Shady Path

{d}(scroll up for more){dff}
''')
        choosenClass = input("\n> ")
        clear()

        if choosenClass == "1" or choosenClass == "2" or choosenClass == "3" or choosenClass == "Ncoord": break

    # -----------------------------------------------------------------------------
    match choosenClass: # Set the correct value of the class variable

        case "1": # Soldier
            c = c3
            player["class"] = classes[0]
            player["hp_max"] = 80 + randint(1, 30)
            player["hp"] = player["hp_max"]
            player["endur"] = randint(round(player["hp_max"] / 2), round(player["hp_max"] * 0.75))
            player["intell"] = randint(20, 50)
            player["salutation"] = "the mighty"

        case "2": # Mage
            c = c6
            player["class"] = classes[1]
            player["hp_max"] = 70 + randint(1, 10)
            player["hp"] = player["hp_max"]
            player["endur"] = randint(round(player["hp_max"] / 5), round(player["hp_max"] / 2))
            player["intell"] = randint(50, 90)
            player["salutation"] = "the powerful"

        case "3": # Thief
            c = c2
            player["class"] = classes[2]
            player["hp_max"] = 100 + randint(1, 50)
            player["hp"] = player["hp_max"]
            player["endur"] = randint(round(player["hp_max"] / 6), round(player["hp_max"] / 3))
            player["intell"] = randint(35, 65)
            player["salutation"] = "the skillful"

        case _: # Undefined
            c = "\033[38;5;222m"
            player["class"] = classes[3]
            player["hp_max"] = 1000
            player["hp"] = player["hp_max"]
            player["endur"] = round(player["hp_max"] * 0.8)
            player["intell"] = 1000
            player["salutation"] = "the"

    # -----------------------------------------------------------------------------
    while True: # draw sreen for accepting name and class

        print_center(f'''
{read_txt(r"ascii\void.txt")}
These are your stats:

{'-' * 28}
Your Name: {player["name"]}
Chosen Class: {c}{player["class"]}{r}
Healthpoint: {player["hp"]}/{player["hp_max"]}
Endurance: {player["endur"]}
Intelligence: {player["intell"]}
{'-' * 28}

{"Is this correct?" if not player["class"] == "Undefined" else "You're about to enter God Mode as the Undefined class.\n\nDo you wish to proceed?"}



(y) Oh, hell yes! Bring it on already!
(n) Hell no. Not a chance!
''')
        is_ok = input("\n> ")
        clear()

        if is_ok == "y":
            asking = False
            played_music.kill()
            playing_music = False

            break
        elif is_ok == "n":
            c = c9
            break

# --------------------- CLEAR TERMINAL AND SET CONSOLE COLOR ---------------------
print(f"{c}")
clear()

# ----------------------------- SET THE FIRST IMAGE ------------------------------

img = read_txt(r"ascii\room1.txt")

# ----------------- START PLAYING MUSIC WHEN ENTERING GAME ROOM ------------------

if not playing_music:
    played_music = subprocess.Popen(["python", "music.py", r"music\loophero.wav", str(int(True))])
    playing_music = True

# -------------------------- RUNNING THE MAIN GAME LOOP --------------------------

while running: # THE GAME LOOP
    # Set healtpoint limit -------------------------------------------------------
    player["hp"] = player["hp_max"] if player["hp"] > player["hp_max"] else player["hp"]

    # Break the while loop if the player is dead ---------------------------------
    if player["hp"] <= 0:
        # Play sound
        subprocess.Popen(["python", "music.py", "sound/gameover.wav", str(int(False))])
        # Game over screen
        print_center(f'''
        
        
        - GAME OVER -
        
        
        
        Press enter to leave the game...''')
        input()
        cmd(r)
        clear()
        break

    # Break the while loop if the player wins -------------------------------------
    if win == True:
        # Winner screen
        print_center(f'''
        - You Won! -
        ''')
        break

    # GAME ------------------------------------------------------------------------
    match event: # Handling events
        # -------------------------------------------------------------------------
        case "Default": # Default event - game intro

            # Main page - Character sheet
            print_center(f'''
{img}
{description}

(1) Try open the door (exit game)
{"(2) Inspect the chest" if not chest1_found else f"{d}(2) Inspect again the chest{dff}"}
{"(3) Stop playing the music" if playing_music else f"{d}(3) Stop playing the music{dff}"}

{'-' * 50}
Hp: {player["hp"]}/{player["hp_max"]} | End: {player["endur"]} | Int: {player["intell"]} | Inv: {len(inventory)} items
{'-' * 50}
{b}[{player["name"]} {player["salutation"]} {player["class"]}]{bff}
''')
            choice = input("\n> ")

            match choice:
                case "1":
                    event = "Door"
                case "2":
                    event = "Chest"
                case "3":
                    played_music.kill()
                    playing_music = False
                case "i":
                    previous_event = event
                    event = "Inventory"
            clear()

        # -------------------------------------------------------------------------
        case "Door":
            print_center(f'''
{read_txt(r"ascii\door1_v3.txt")}

You entered the door.



{text[press_enter]}
''')
            input()
            event = "Default"
            img = read_txt(r"ascii\room2.txt")
            clear()

        # -------------------------------------------------------------------------
        case "Chest":
            while True:
                if not chest1_found:
                    print_center(f'''
{read_txt(r"ascii\chest1.txt")}
{eventDescription[inspect_chest]}


(y) Yes, definitely
(n) No, it's too suspicious
''')
                    choice = input("> ")

                    if choice != "":
                        if choice == "y":
                            _case = (choose_from([Case_SimpleTrap, Case_SimpleChest]))
                            match _case["type"]:
                                case "Chest":
                                    event = "Found_Item1"
                                case "Trap":
                                    event = "Simple_Trap1"
                            #chest1_found = True
                            break
                        elif choice == "n":
                            event = "Default"
                            break
                        elif choice == "i":
                            previous_event = event
                            event = "Inventory"
                            break
                    clear()

                else:
                    print_center(f'''
{read_txt(r"ascii\void.txt")}

{eventDescription[opened_chest_in_dark_room]}
{text[found_nothing]}



{text["press_enter"]}''')
                    #description += f"~ ~ ~{eventDescription["opened_chest_in_dark_room"]}\n{text["found_nothing"]}\n"
                    input()
            clear()
        case "Inventory":

            openInventory(inventory, player)

            input()
            clear()
            event = previous_event

        case "Goblin1":

            player["hp"] -= randint(1, 30)

            print_center(f'''{read_txt(r"ascii\void.txt")}{c1}A goblin hit your head, it hurts...{c}''')

            description += "\nA goblin hit your head, it hurts...\n"

            input()
            clear()
            event = "Default"

        case "Found_Item1":

            items = [Weapon_ShortDagger, Weapon_DwarfHammer, Item_Skull, HealItem_BigPotion,
                     HealItem_SmallPotion, Item_Papper, Weapon_MagicWand, Armor_MysticArmor]
            _item = choose_from(items)
            description += eventDescription[open_chest_in_dark_room]
            inventory.append(_item)

            print_center(f'''
{read_txt(get_item_image(_item[name]))}
{eventDescription[open_chest_in_dark_room]}

{text["found_common"]} {_item[name]}
''')

            input()
            clear()
            event = "Default"

        case "Simple_Trap1":

            player["hp"] -= randint(1, 10)

            description += "\nIt's a trap inside of the chest!\n"

            print_center(f'''
{read_txt(r"ascii\void.txt")}
{c1}It's a trap inside of the chest!{c}
''')

            input()
            clear()
            event = "Default"



played_music.kill()





