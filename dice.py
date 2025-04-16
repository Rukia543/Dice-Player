"""
    dice.py             Author: Chris Kelly (based on Die.java by Lewis/Loftus)

    Represents one die (singular of dice) with faces showing values
    between 1 and 6.
"""

import random

class Die (object):

    # maximum face value
    MAX = 6    

    # Constructor: Sets the initial face value.
    def __init__ (self):
        self.__face_value = 1

    def __str__(self):
        return str(self.__face_value)

    @property
    def face_value(self):
        return self.__face_value
        # if self.__face_value % 2 == 0:
        #     return "Even"
        # else:
        #     return "Odd"

    #    Face value mutator.
    @face_value.setter
    def face_value(self, new_face_value):
        if 1 <= new_face_value and new_face_value <= Die.MAX:
            self.__face_value = new_face_value
        else:
            print ("New face value must be between 1 and", Die.MAX, end=".\n")

    #    Rolls the die and returns the result.
    def roll (self):
        self.__face_value = random.randint(1, Die.MAX)
        return self.__face_value