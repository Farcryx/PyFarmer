from src.classes.Player import Player


class DiceEventHandler:
    def __init__(self, main_herd: dict[str, int]):
        self.main_herd = main_herd
        self.last_roll = ("", "")
        self.player = None
    
    def handle_roll(self, dice1_result: str, dice2_result: str, player: Player) -> tuple[bool, str]:
        """
        Handle dice roll event
        :param dice1_result: Result of the first dice roll
        :param dice2_result: Result of the second dice roll
        :param player: Player object
        :return: Tuple with two elements: boolean if the game should continue and message for the player
        """
        self.player = player
        self.last_roll = (dice1_result, dice2_result)
        
        # Check for wolf or fox
        if "wolf" in (dice1_result, dice2_result):
            return self._handle_wolf()
        if "fox" in (dice1_result, dice2_result):
            return self._handle_fox()
            
        # Count animals from the roll and update player's herd
        animals_to_add = self._count_animals_from_roll()
        return self._update_player_herd(animals_to_add)
    
    def _handle_wolf(self) -> tuple[bool, str]:
        """Wolf event handler"""
        if self.player.big_dogs > 0:
            return True, "Wolf was scared away by big dog!"
        
        # Player lost all animals except horses
        lost_animals = {k: v for k, v in self.player.animals.items() if k != "horse"}
        self.player.animals.update({k: 0 for k in lost_animals.keys()})
        return False, "Wolf ate all animals except horses!"
    
    def _handle_fox(self) -> tuple[bool, str]:
        """Fox event handler"""
        if self.player.small_dogs > 0:
            return True, "Fox was scared away by small dog!"
        
        # Player lost all rabbits
        lost_rabbits = self.player.animals.get("rabbit", 0)
        self.player.animals["rabbit"] = 0
        return False, f"Fox ate all the rabbits! ({lost_rabbits})"
    
    def _count_animals_from_roll(self) -> dict[str, int]:
        """Count animals from the last roll"""
        animals = {}
        for result in self.last_roll:
            if result not in ("wolf", "fox"):
                animals[result] = animals.get(result, 0) + 1
        return animals
    
    def _update_player_herd(self, new_animals: dict[str, int]) -> tuple[bool, str]:
        """Update player's herd with new animals"""
        message = []
        for animal, count in new_animals.items():
            available = self.main_herd.get(animal, 0)
            if available >= count:
                self.player.animals[animal] = self.player.animals.get(animal, 0) + count
                self.main_herd[animal] -= count
                message.append(f"+{count} {animal}")
                
        return True, ", ".join(message) if message else "No animals to take!"
