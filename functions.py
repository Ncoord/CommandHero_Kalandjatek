
import os
import shutil
import re
from pathlib import Path
from random import randint
from msvcrt import *

def random_percent():
    randomNum = randint(0,100)
    return randomNum

def input_r():
    while True:
        if kbhit():
            key = str(getwch())
            return key

def get_path():
    BASE_DIR = Path(__file__).resolve().parent
    return BASE_DIR

def read_txt(txt_file):
    with open(get_path() / txt_file, "r", encoding="utf-8") as text:
        return text.read()

def cmd(command):
    os.system(command)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_center(text):
    width = shutil.get_terminal_size().columns
    ansi = re.compile(r'\033\[[0-9;]*m')

    for line in text.splitlines():
        print(' ' * ((width - len(ansi.sub('', line))) // 2)+ line)


# ------------------------------- EVENT FUNCTIONS --------------------------------

def eventEnemy(playerHealth, damage):
    playerHealth -= damage
    return playerHealth

def openChest():
    num = random_percent()
    return num

def openDoor():
    return