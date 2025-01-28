from src.classes.MainHerd import MainHerd

class Player:
    def __init__(self, name: str, main_herd: MainHerd) -> None:
        self.name = name
        self.animals = {"rabbit": 0, "sheep": 0, "pig": 0, "cow": 0, "horse": 0, "small_dog": 0, "big_dog": 0}
        self.current_dice_roll = ("", "")
        self.total_pairs = {"rabbit": 0, "sheep": 0, "pig": 0, "cow": 0, "horse": 0}
        self.has_won = False
        self.main_herd = main_herd

    def add_animal(self, animal_type: str, quantity: int = 1) -> bool:
        """Add animals to player's herd"""
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
            # remove animals from main herd
            self.main_herd.remove_animal(animal_type, quantity)
            self.check_pairs()
            self._check_win_condition()
            return True
        return False

    def remove_animal(self, animal_type: str, quantity: int = 1) -> bool:
        """Remove animals from player's herd"""
        if animal_type in self.animals and self.animals[animal_type] >= quantity:
            self.animals[animal_type] -= quantity
            # add animals to main herd
            self.main_herd.add_animal(animal_type, quantity)
            self.check_pairs()
            return True
        return False

    def check_pairs(self):
        """Check and update animal pairs"""
        for animal in self.animals:
            pairs = self.animals[animal] // 2
            self.total_pairs[animal] = pairs

    def _check_win_condition(self):
        """Check if player has won"""
        required_animals = {"rabbit": 1, "sheep": 1, "pig": 1, "cow": 1, "horse": 1}
        self.has_won = all(self.animals[animal] >= quantity 
                          for animal, quantity in required_animals.items())

    def reset(self):
        """Reset player state"""
        self.animals = {k: 0 for k in self.animals}
        self.current_dice_roll = ("", "")
        self.total_pairs = {k: 0 for k in self.total_pairs}
        self.has_won = False

    def __str__(self) -> str:
        """String representation of player's state"""
        animals_str = ", ".join(f"{k}: {v}" for k, v in self.animals.items())
        return f"Player: {self.name} | {animals_str}"

    def get_last_roll(self) -> str:
        """Return the last roll of the player"""
        return f"{self.name} rolled {self.current_dice_roll[0]} and {self.current_dice_roll[1]}"

    def get_number_of_animal(self, animal: str) -> int:
        """Return the number of a specific animal"""
        return self.animals[animal]