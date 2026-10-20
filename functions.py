
import os
import shutil
import re
from pathlib import Path
from msvcrt import *
from random import choices
from ansi_esc_codes import *


def choose_from(list_of_items):
    weights = [item["rarity"] for item in list_of_items]

    chosen_item = choices(list_of_items, weights=weights, k=1)[0]

    return chosen_item

def input_r(expected, exclusion):
    while True:

        text = ""
        while True:

            if kbhit():

                key = getch()

                if key in expected:
                    if len(text) == 0:
                        text += key.decode("utf-8")
                    else:
                        text = text[:-1]
                        text += key.decode("utf-8")

                elif key in exclusion:
                    text = key.decode("utf-8")
                    #return text

                elif key == b"\r":
                    return text
                print(text, end="\r")





def get_path():
    BASE_DIR = Path(__file__).resolve().parent
    return BASE_DIR

def read_txt(txt_file):
    with open(get_path() / txt_file, "r", encoding="utf-8") as text:
        return text.read()

def cmd(command):
    os.system(command)

def clear():
    os.system('cls')

def print_center(text):
    width = shutil.get_terminal_size().columns
    ansi = re.compile(r'\033\[[0-9;]*m')

    for line in text.splitlines():
        print(' ' * ((width - len(ansi.sub('', line))) // 2)+ line)

def get_item_image(itemname):
    img = ""
    match itemname:
        case "Short Dagger":
            img = r"ascii\void.txt"

    return img



# ------------------------------- EVENT FUNCTIONS --------------------------------

def eventEnemy(playerHealth, damage):
    playerHealth -= damage
    return playerHealth

def openChest():
    return

def openDoor():
    return

def openInventory(inventory,player):
    for item in inventory:

        if item["type"] == "Weapon" or item["type"] == "Armor":
            _name = item["name"]
            _rar = item["rarity"]
            _str = item["req_streng"]
            _int = item["req_intell"]
            _dmg = item["damage"]
            _def = item["defense"]
            _req = ""

            if _str - player["endur"] > 0:
                _req += "\nrequires +" + str(_str - player["endur"]) + " END."

            if _int - player["intell"] > 0:
                _req += "\nrequires +" + str(_int - player["intell"]) + " INT."

            if _str > player["endur"] or _int > player["intell"]:
                _name = f"{d}({_rar}%) {s}{_name}{sff}"
            else:
                _name = f"({_rar}%) {_name}\ndeals {_dmg} dmg\ngives {_def} def"

            print_center(f"\n{_name}{_req}{dff}")
        elif item["type"] == "HealItem":
            _name = item["name"]
            _rar = item["rarity"]
            _heal = item["healing"]
            print_center(f"\n({_rar}%) {_name}\nheals {_heal} hp")

        elif item["type"] == "Misc":
            _name = item["name"]
            _rar = item["rarity"]
            print_center(f"\n({_rar}%) {_name}")
