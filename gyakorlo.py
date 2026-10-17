
"""
class vechile:
    def __init__(self, brand, current_speed, max_speed):
        self.brand = brand
        self.current_speed = current_speed
        self.max_speed = max_speed

    def accelerate(self, value):
        self.current_speed += value
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        return self.current_speed

    def brake(self, value):
        self.current_speed -= value
        if self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed


my_vechile = vechile("Toyota", 20, 100)

print(my_vechile.brand)           # Toyota
print(my_vechile.accelerate(30))   # 50
print(my_vechile.accelerate(120))  # 100
print(my_vechile.brake(15))        # 85
print(my_vechile.brake(100))       # 0


from enum import Enum

class randomname(Enum):
    RED: str = "R"
    GREEN: str = "G"
    BLUE: str = "B"
"""
from unittest import result

"""

import shutil

from functions import clear

clear()

while True:
    width = shutil.get_terminal_size().columns

    text = f'''
    1 -> Enemy
    2 -> Chest
    3 -> Door
    '''

    for line in text.splitlines():
        print(line.center(width))


    clear()


import subprocess

help(subprocess)                  # Mire való?
print(dir(subprocess))             # Milyen neveket tartalmaz?
help(subprocess.run)               # Hogyan használható egy konkrét függvény?


repeat = bool(int("1"))
print(type(repeat),repeat)

"""

'''
pontok = {}

while True:
    name = input("Mi a neved?\n> ")

    value = input("Mi a pontszámod?\n> ")

    pontok[name] = value

    print(pontok.items())

    if int(pontok[name]) < 20:
        print(pontok[name], "- Bukta\n")
    else:
        print("Átmentél\n")

    choice = input("Abba hagyod a dolgot? (STOP)\n\n> ")
    if choice == "STOP":
        break

'''

#from functions import input_r

#print("> ")

#input_r()

from items import *
from random import randint

def random_item(list):
    weapons = []
    for item in list:
        weapons.append(weapon_data[item]["name"])

    number = randint(0, len(weapons)-1)

    return weapons[number]

print(random_item(weapon_data))