import random


class Dice:
    def __init__(self, sides: list[str], dice_type: str, seed: int = None):
        self.sides = sides
        self.dice_type = dice_type
        self.roll_result = ""
        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)

    def roll(self) -> str:
        """Wykonuje rzut kostką i zwraca wynik"""
        self.roll_result = random.choice(self.sides)
        return self.roll_result

    def reset(self):
        """Resetuje wynik rzutu"""
        self.roll_result = ""

    def __str__(self) -> str:
        return f"Dice {self.dice_type}: {self.roll_result}"