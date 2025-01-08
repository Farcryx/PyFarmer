class Player:
    def __init__(self, name: str):
        self.name = name
        self.animals = {"królik": 0, "owca": 0, "świnia": 0, "krowa": 0, "koń": 0}
        self.small_dogs = 0
        self.big_dogs = 0
        self.current_dice_roll = ("", "")
        self.total_pairs = {"królik": 0, "owca": 0, "świnia": 0, "krowa": 0, "koń": 0}
        self.has_won = False

    def add_animal(self, animal_type: str, quantity: int = 1) -> bool:
        """Add animals to player's herd"""
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
            self._check_pairs()
            self._check_win_condition()
            return True
        return False

    def remove_animal(self, animal_type: str, quantity: int = 1) -> bool:
        """Remove animals from player's herd"""
        if animal_type in self.animals and self.animals[animal_type] >= quantity:
            self.animals[animal_type] -= quantity
            self._check_pairs()
            return True
        return False

    def _check_pairs(self):
        """Check and update animal pairs"""
        for animal in self.animals:
            pairs = self.animals[animal] // 2
            self.total_pairs[animal] = pairs

    def _check_win_condition(self):
        """Check if player has won"""
        required_animals = {"królik": 1, "owca": 1, "świnia": 1, "krowa": 1, "koń": 1}
        self.has_won = all(self.animals[animal] >= quantity 
                          for animal, quantity in required_animals.items())

    def reset(self):
        """Reset player state"""
        self.animals = {k: 0 for k in self.animals}
        self.small_dogs = 0
        self.big_dogs = 0
        self.current_dice_roll = ("", "")
        self.total_pairs = {k: 0 for k in self.total_pairs}
        self.has_won = False

    def __str__(self) -> str:
        """String representation of player's state"""
        animals_str = ", ".join(f"{k}: {v}" for k, v in self.animals.items())
        dogs_str = f"Małe psy: {self.small_dogs}, Duże psy: {self.big_dogs}"
        return f"Gracz {self.name} | {animals_str} | {dogs_str}"