
from ansi_esc_codes import *

# ------------------------------ EVENT DESCRIPTIONS -------------------------------

#Do not write any longer text than below describen!

"""
Default event descriptionDefault event description!
"""

eventDescription = {
    "greeting" : f'''{i}
Greetings, adventurer!

This is a short RPG {u}console game{uff}. Prepare yourself 
for a fictional journey through a dungeon, where   
your goal is to escape safely and unharmed.        
~ ~ ~
The story may be linear, but no two runs will be   
the same. Enemies and items are {u}randomized{uff},        
so adapt to your surroundings and make the         
most of what you find.                             
{iff}''',
    "what_is_name": f'''
Speak your name, adventurer — what shall be engraved
upon your tombstone when your journey ends...
''',
    "default_event": f'''
Default event descriptionDefault event description!
Default event descriptionDefault event description!
~ ~ ~
Default event descriptionDefault event description!
Default event descriptionDefault event description!
''',
    "soldier_class": f'''{i}
Soldiers are the iron walls between life and death.
Forged through endless battles and merciless train-
ing, they have {u}immense endurance{uff} and the {u}strength{uff}  
to withstand wounds that would cripple lesser men. 
Their minds may {u}lack the cunning{uff} of others, but    
few can match their resolve when steel meets flesh.
~ ~ ~
A soldier {u}doesn't rely on wit{uff}. They endure, strike,
and stand their ground when all hope seems lost.   
In the depths of the dungeon, where fear devours   
the weak, raw strength may be the only thing       
standing between you and an untimely grave.        
{iff}''',
    "mage_class": f'''{i}
Magicians seek knowledge beyond the boundaries of  
mortal understanding. Their minds pierce mysteries 
that others dare not question, {u}wielding arcane{uff}     
forces that twist the very laws of nature.         
However, their {u}knowledge generally exceed{uff}          
their physical strength.                           
~ ~ ~
Fragile in body but unmatched in {u}intellect{uff},        
a magician must rely on wisdom where others rely on
steel. Their {u}endurance is fleeting{uff}, and even a     
minor wound may prove fatal. In the darkness below,
one clever decision may achieve what a hundred     
swords cannot — But even {u}small mistakes{uff} can be     
{u}fatal{uff}. Care and focus are their best friends.      
{iff}''',
    "thief_class": f'''{i}
Thieves thrive where trust is scarce and death     
lurks behind every shadow. Neither as mighty as    
soldiers nor as wise as magicians, they survive    
through {u}cunning{uff}, instinct, and an unshakable will  
to live. Their {u}resilience is remarkable{uff}, allowing  
them to endure dangers that would bring others     
to their knees.                                    
~ ~ ~
A thief knows that honor cannot stop a blade, and  
knowledge alone cannot save a life. They watch,    
adapt, and seize every opportunity, no matter how  
grim the cost. In the dungeon, {u}survival{uff} belongs to 
those who know {u}when to fight{uff} — and {u}when to flee{uff}.   
{iff}''',
    "open_chest_in_dark_room": f'''
In the dark room, you could barely make out the   
corner. You approached the chest and easily lifted
its heavy lid. Despite the damp, moist wood, curi-
osity led you to open it, revealing an item.      
''',
    "opened_chest_in_dark_room": f'''
You crawl back to the chest from earlier and look 
for clues, but find nothing more than an empty    
chest that mirrors your state in the dark room:   
''',
"inspect_chest": f'''
You see a old-looking chest, you lean forward for
inspecting more of it. Could be useful the content.
You try to open the chest, or leave it as it is?
'''
}

text = {
"title": r"----- T h e  -  A d v e n t u r e  -  G a m e -----",
"soldier_title": "The class of the strongest warriors",
"mage_title": "The mysterious art of magic",
"thief_title": "The class of cunning thieves",
"found_common": "You've got:",
"found_nothing": "Empty — just like your soul...",
"press_enter": f"Press {b}[enter]{bff} to continue...",
"try_again": f"Press {b}[enter]{bff} to try again...",
"invalid_name": "Your name can't be nothing?!",
"choose_class": "You may now choose your class:"
}


# Set default event description
description = eventDescription["default_event"]