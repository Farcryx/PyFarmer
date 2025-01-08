import random

class Dice:
    def __init__(self, sides: list[str], dice_type: str, seed: int = None):
        self.sides = sides
        self.dice_type = dice_type
        self.roll_result = ""
        self.seed = seed if seed else random.randint(0, 1000)
    
    def roll(self) -> str:
        """Wykonuje rzut kostką i zwraca wynik"""
        random.seed(self.seed)
        self.roll_result = random.choice(self.sides)
        return self.roll_result
    
    def reset(self):
        """Resetuje wynik rzutu"""
        self.roll_result = ""
        
    def __str__(self) -> str:
        return f"Kostka {self.dice_type}: {self.roll_result}"