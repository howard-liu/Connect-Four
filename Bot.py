from Player import *
import random

class Bot(Player):

    def __init__(self, number):
        super().__init__(number)

    @staticmethod
    def input_column():
        return random.randint(1, 7)
