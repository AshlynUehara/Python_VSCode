import random


class Dice:
    def roll(self):
        # returns a tuple of two random values
        numbers = (random.randint(1,6),random.randint(1,6))
        return numbers


first_round = Dice()
print(first_round.roll())