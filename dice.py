import random

class Dice():
    '''initialize attribute for sides. Default value of dice is 6'''
    def __init__(self,sides = 6):
        self.sides = sides

    def describe_dice(self):
        '''print how many sides the die has'''
        print("this die has " + str(self.sides) + " sides!")

    def roll_dice(self):
        roll_count = 0
        print("rolling 10 times...")
        for rolls in range(1, self.sides + 1):
            roll_count += 1
            roll = random.randint(1, self.sides)
            print(f"roll {roll_count}: {roll}")

