"""
    File: die_cli.py
    Author: Chris Kelly
    Course: CS110, Spring 2016
    Description: Serves as a user interface for playing
        a dice game according to the special rules here.
"""

exec(open("./dice_player.py").read())
  
# Replace MyName with your own name
me = DicePlayer("Rukia")
repeat = True
input ("Press Enter to roll.")

while repeat:
    me.roll()
    repeat = input("Type 'yes' to go again: ").lower() == "yes"

print ("\nGame over...")
print (me.final_scores())