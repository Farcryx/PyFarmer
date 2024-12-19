import random


class Dice:
    def __init__(self, sides: list[str], dice_type: str, seed: int = None):
        self.sides = sides
        self.dice_type = dice_type
        self.roll_result = ""
        self.seed = seed if seed else random.randint(0, 1000)
