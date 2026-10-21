
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
from operator import index
from shlex import split, join

import items

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

"""
from items import *
from random import randint

items = [
    Weapon_DwarfHammer,
    Weapon_GreatSword,
    Weapon_MagicWand,
    Weapon_ShortDagger,
    Weapon_SpikySpear,
    Weapon_WideShield,
    Armor_MysticArmor,
    Item_Ash,
    Item_Dust,
    Item_Leather,
    Item_Papper,
    Item_Pebble,
    Item_Skull,
    HealItem_BigPotion,
    HealItem_SmallPotion
]

def random_item(list_of_items):
    percentage_sum = 1
    rarity_sum = 0
    intervals = []
    chosen_item = None

    for item in list_of_items:
        rarity_sum += (item["rarity"])

    for item in list_of_items:
        new_percent = round((item["rarity"] * 10000) / rarity_sum)

        interval = range(percentage_sum, percentage_sum + new_percent)
        percentage_sum += new_percent

        intervals.append(interval)

    random_num = randint(1, percentage_sum)

    for interval in intervals:
        if random_num in interval:
            itemindex = intervals.index(interval)

            print(f'''
Random szám: {random_num} a "{interval}" {str(itemindex + 1)}. elemszámú tartományban.
Maximális tartományérték: {percentage_sum}%
''')

            chosen_item = list_of_items[itemindex]

    print(f"\n{chosen_item['name']} {chosen_item['rarity']}%")

random_item(items)

"""


from functions import input_r, print_center


key = input_r([b"1", b"2", b"3", b"i"])

print_center(f"{key.decode("utf-8")}: got returned")