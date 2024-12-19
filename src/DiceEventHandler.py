class DiceEventHandler:
    def __init__(self, main_herd: dict[str, int], player_animals: dict[str, int], player_dogs: dict[str, int]):
        self.main_herd = main_herd
        self.player_animals = player_animals
        self.player_dogs = player_dogs
        self.last_roll = ("", "")
