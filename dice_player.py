"""
    File: dice_player.py
    Author: Chris Kelly
    Course: CS110, Summer 2023
    Description: Represents one of two players in 
        a dice game, scored according to the special 
        rules here.
"""

exec(open("./dice.py").read())

class DicePlayer:

    def __init__ (self, player_name, set_other=True):
        self.__other = None
        self.__die1 = Die()
        self.__die2 = Die()
        self.__name = player_name
        self.__score = 0
        self.__roll_num = 1
        if set_other:
            self.__other = DicePlayer("The computer", False)
            self.__other.other = self

    @property
    def name (self):
        return self.__name

    @property
    def score (self):
        return self.__score

    @score.setter
    def score (self, new_score):
        self.__score = new_score

    @property
    def other (self):
        # print ("Cannot return reference to opponent directly")
        return self.__other

    @other.setter
    def other (self, new_other):
        if self.__other == None:
            self.__other = new_other
        else:
            print ("Error: This player already has an other")

    def roll(self):
        print ("\n==============Roll #" + str(self.__roll_num) + "==============")
        self.do_roll()
        print (self.present_scores() + '\n')
        self.__other.do_roll()
        print (self.present_scores() + '\n')
        self.__roll_num += 1

    def present_scores (self):

        other = self.__other
        current_leader = ""

        # Your code starts HERE
        # Rules to follow before playing this game.

    def roll(self):
     for roll_num in range(1, 13):
        print("\n==============Roll #" + str(self.__roll_num) + "==============")
        die1_value = self.__die1.roll()
        die2_value = self.__die2.roll()
        total = die1_value + die2_value
        diff = abs(die1_value - die2_value)

        if die1_value > die2_value:
            if diff % 2 == 1:
                self.__score -= diff
                self.other.score += diff
                print("You decreased Rukia's score by " + str(diff) + " and increased the computer's score.")
            else:
                self.__score += diff
                self.other.score -= diff
                print("You increased Rukia's score by " + str(diff) + " and decreased the computer's score.")
        elif die2_value > die1_value:
            if diff % 2 == 1:
                self.__score += diff
                self.other.score -= diff
                print("You increased Rukia's score by " + str(diff) + " and decreased the computer's score.")
            else:
                self.__score -= diff
                self.other.score += diff
                print("You decreased Rukia's score by " + str(diff) + " and increased the computer's score.")

        if (die1_value == die2_value):
            factors = []
            for factor in range(1, total):
                if total % factor == 0:
                    factors.append(factor)
            score = sum(factors)
            self.__score += score
            print("Special rule activated! Score increased by: " + str(score))
        print(self.present_scores())
        self.__roll_num += 1


    def present_scores(self):
        other = self.__other
        current_leader = ""

        if self.__score > other.score:
            current_leader = self.__name
        elif self.__score < other.score:
            current_leader = other.name
        else:
            current_leader = "Actually, it's a tie!"

        return "My Score: " + str(self.__score) + \
            "\nOpponent Score: " + str(other.score) + \
            "\nCurrent Leader: " + current_leader

    def final_scores(self):
        other = self.__other
        if self.__score > other.score:
            return f"{self.__name} wins!"
        elif self.__score < other.score:
            return f"{other.name} wins!"
        else:
            return "It's a tie!"


# Print out final scores
me = DicePlayer("Player 1")
me.roll()
print(me.final_scores())

