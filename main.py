
# --------------------------- IMPORTING THE MAIN MODULS ---------------------------

import os
import shutil
from random import randint
from functions import *
from descriptions import *
from variables import *
import subprocess
from items import *
from cases import *

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

{text["title"]}


        
{eventDescription["greeting"]}
{eventDescription["what_is_name"]}
''')
        playerName = input("\n> ")
        clear()

        if playerName != "": break
        else:
            print_center(f'''
{read_txt(r"ascii\void.txt")}
{c1}{text["invalid_name"]}



{text["try_again"]}{r}{c}''')
            input("\n> ")
            clear()

    # -----------------------------------------------------------------------------
    while True: # Draw a screen for choosing a class
        print_center(f'''
{c3}{b}[{text["soldier_title"]}]{bff}
{read_txt(r"ascii\soldier.txt")}
{eventDescription["soldier_class"]}{r}

{c6}{b}[{text["mage_title"]}]{bff}
{read_txt(r"ascii\mage.txt")}
{eventDescription["mage_class"]}{r}

{c2}{b}[{text["thief_title"]}]{bff}
{read_txt(r"ascii\thief.txt")}
{eventDescription["thief_class"]}{r}




{text["choose_class"]}

{c3}(1){r} The Honorable Path of Soldiers
{c6}(2){r} Mysterious Beings — The Magicians
{c2}(3){r} The Thieves' Shady Path

{d}(scroll up for more){dff}
''')
        choosenClass = input("\n> ")
        clear()

        if choosenClass == "1" or choosenClass == "2" or choosenClass == "3": break

    # -----------------------------------------------------------------------------
    match choosenClass: # Set the correct value of the class variable

        case "1": # Soldier
            playerClass = classes[0]
            c = c3
            healthpointMax = 80 + randint(1, 30)
            healthpoint = healthpointMax
            endurance = randint(round(healthpointMax / 2), round(healthpointMax * 0.75))
            intelligence = randint(20, 50)

        case "2": # Mage
            playerClass = classes[1]
            c = c6
            healthpointMax = 70 + randint(1, 10)
            healthpoint = healthpointMax
            endurance = randint(round(healthpointMax / 5), round(healthpointMax / 2))
            intelligence = randint(50, 90)

        case "3": # Thief
            playerClass = classes[2]
            c = c2
            healthpointMax = 100 + randint(1, 50)
            healthpoint = healthpointMax
            endurance = randint(round(healthpointMax / 6), round(healthpointMax / 3))
            intelligence = randint(35, 65)

        case _:
            playerClass = classes[4]    # Undefined

    # -----------------------------------------------------------------------------
    while True: # draw sreen for accepting name and class

        print_center(f'''
{read_txt(r"ascii\void.txt")}
These are your stats:

{'-' * 28}
Your Name     |   {playerName}
Chosen Class  |   {c}{playerClass}{r}
Healthpoint   |   {healthpoint}/{healthpointMax}
Endurance     |   {endurance}
Intelligence  |   {intelligence}
{'-' * 28}

Is this correct?



(y) Oh hell yes, bring it on already!
(n) Definitely a no! 
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

# ------------------------ DEFINE LABEL FOR PLAYER'S TITLE ------------------------

if playerClass == "Mage":
    lable = "the powerful"
if playerClass == "Soldier":
    lable = "the mighty"
if playerClass == "Thief":
    lable = "the skillful"

# --------------------- CLEAR TERMINAL AND SET CONSOLE COLOR ---------------------

cmd(c)
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
    healthpoint = healthpointMax if healthpoint > healthpointMax else healthpoint

    # Break the while loop if the player is dead ---------------------------------
    if healthpoint <= 0:
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
{b}[{playerName} {lable} {playerClass}]{bff}
{'-' * 50}
HP: {healthpoint}/{healthpointMax} | END : {endurance} | INT : {intelligence}
{'-' * 50}
{img}
{description}


(1) Try open the door (exit game)
{"(2) Inspect the chest" if not chest1_found else f"{d}(2) Inspect again the chest{dff}"}
{"(3) Stop playing the music" if playing_music else f"{d}(3) Stop playing the music{dff}"}
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
            clear()

        # -------------------------------------------------------------------------
        case "Door":
            print_center(f'''
{read_txt(r"ascii\door1_v3.txt")}

You entered the door.



{text["press_enter"]}
''')
            input()

            event = "Default"
            img = read_txt(r"ascii\room2.txt")
            healthpoint = 0

            clear()

        # -------------------------------------------------------------------------
        case "Chest":
            while True:
                if not chest1_found:
                    print_center(f'''
{read_txt(r"ascii\chest1.txt")}{eventDescription["inspect_chest"]}


(y) Yes, definitely
(n) No, it's too suspicious
''')
                    choice = input("> ")

                    if choice != "":
                        if choice == "y":
                            _case = (choose_from([Case_SimpleTrap, Case_SimpleChest, Case_EnemyGoblin]))
                            match _case["type"]:
                                case "Chest":
                                    event = "Found_Item"
                                case "Trap":
                                    event = "Trap"
                                case "Goblin":
                                    event = "Enemy"
                            break
                        elif choice == "n":
                            event = "Default"
                            break
                    clear()

                else:
                    print_center(f'''
{read_txt(r"ascii\void.txt")}

{eventDescription["opened_chest_in_dark_room"]}
{text["found_nothing"]}



{text["press_enter"]}''')
                    description += f"~ ~ ~{eventDescription["opened_chest_in_dark_room"]}\n{text["found_nothing"]}\n"
                    input()
            clear()
        case "Menu_Items":

            items = [Weapon_ShortDagger, HealItem_BigPotion, Item_Skull, Item_Papper, HealItem_SmallPotion, Item_Ash,
                     Item_Dust]

            for item in items:

                name = item["name"]
                _rar = item["rarity"]
                _str = item["required_strength"]
                _int = item["required_intelligence"]
                requirement = ""

                if _str - endurance > 0:
                    requirement += "\nrequires +"+str(_str - endurance)+" END."

                if _int - intelligence > 0:
                    requirement +="\nrequires +" + str(_int - intelligence) + " INT."

                if _str > endurance or _int > intelligence:
                    name = f"{d}({_rar}%) {s}{name}{sff}"
                else:
                    name = f"({_rar}%) {name}"

                print_center(f"\n{name}{requirement}{dff}")

            input()
            clear()

        case "Enemy":

            healthpoint -= randint(1, 30)

            print_center(f'''{read_txt(r"ascii\void.txt")}{c1}ENEMY{c}''')

            description += "\nGoblins got your head, it hurts...\n"

            input()
            clear()
            event = "Default"

        case "Found_Item":

            items = [Weapon_ShortDagger, HealItem_BigPotion, Item_Skull, Item_Papper, HealItem_SmallPotion,
                     Item_Ash, Item_Dust]

            _item = choose_from(items)["name"]

            description += eventDescription["open_chest_in_dark_room"]

            inventory.append(_item)

            print_center(f'''
{read_txt(r"ascii\void.txt")}
{eventDescription["open_chest_in_dark_room"]}

{text["found_common"]} {_item}


{inventory}
''')

            input()
            clear()
            event = "Default"

        case "Trap":

            healthpoint -= randint(1, 10)

            description += "\nIt's a trap inside of the chest!\n"

            print_center(f'''
{read_txt(r"ascii\void.txt")}
{c1}It's a trap inside of the chest!{c}
''')

            input()
            clear()
            event = "Default"



played_music.kill()

























