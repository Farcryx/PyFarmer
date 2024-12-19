class Player:
    def __init__(self, name: str):
        self.name = name
        self.animals = {"królik": 1, "owca": 0, "świnia": 0, "krowa": 0, "koń": 0}
        self.small_dogs = 0
        self.big_dogs = 0
        self.current_dice_roll = ("", "")
        self.total_pairs = {"królik": 0, "owca": 0, "świnia": 0, "krowa": 0, "koń": 0}
        self.has_won = False
