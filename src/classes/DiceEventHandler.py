from src.classes.Player import Player
from src.classes.MainHerd import MainHerd


class DiceEventHandler:
    def __init__(self, main_herd: MainHerd) -> None:
        self.main_herd = main_herd
        self.last_roll = ("", "")
        self.player = None
    
    def handle_roll(self, dice1_result: str, dice2_result: str, player: Player) -> tuple[bool, str]:
        """
        Handle dice roll event.
        :param dice1_result: Result of the first dice roll.
        :param dice2_result: Result of the second dice roll.
        :param player: Player object.
        :return: Tuple with two elements: boolean if the game should continue and message for the player.
        """
        self.player = player
        self.last_roll = (dice1_result, dice2_result)
        # print main herd
        print(self.main_herd.get_formatted_herd())
        # Check for wolf or fox
        if "wolf" in (dice1_result, dice2_result):
            return self._handle_wolf()
        if "fox" in (dice1_result, dice2_result):
            return self._handle_fox()
        if dice1_result == dice2_result:
            return self._handle_double_roll(dice1_result)
        else:
            return self._handle_single_roll()

    def _handle_wolf(self) -> tuple[bool, str]:
        """Wolf event handler"""
        if self.player.big_dogs > 0:
            return True, "Wolf was scared away by big dog!"

        # Player lost all animals except horses
        lost_animals = {k: v for k, v in self.player.animals.items() if k != "horse"}
        for animal, count in lost_animals.items():
            self.main_herd.herd[animal] += count
        self.player.animals.update({k: 0 for k in lost_animals.keys()})
        return False, "Wolf ate all animals except horses!"

    def _handle_fox(self) -> tuple[bool, str]:
        """Fox event handler"""
        if self.player.small_dogs > 0:
            return True, "Fox was scared away by small dog!"

        # Player lost all rabbits
        lost_rabbits = self.player.animals.get("rabbit", 0)
        self.main_herd.herd["rabbit"] += lost_rabbits
        self.player.animals["rabbit"] = 0
        return False, f"Fox ate all the rabbits! ({lost_rabbits})"

    def _handle_double_roll(self, result: str) -> tuple[bool, str]:
        """Handle double roll event"""
        return self._update_player_herd({result: 1})

    def _handle_single_roll(self) -> tuple[bool, str]:
        self.player.check_pairs()
        animals_to_add = {}
        for animal in self.last_roll:
            if animal in self.player.total_pairs and self.player.total_pairs[animal] > 0:
                animals_to_add[animal] = self.player.total_pairs[animal]
        return self._update_player_herd(animals_to_add)

    def _update_player_herd(self, new_animals: dict[str, int]) -> tuple[bool, str]:
        """Update player's herd with new animals"""
        message = []
        for animal, count in new_animals.items():
            available = self.main_herd.herd.get(animal, 0)
            if available >= count:
                print(f"Adding {count} {animal} to player's herd")
                self.player.animals[animal] = self.player.animals.get(animal, 0) + count
                self.main_herd.herd[animal] -= count
                message.append(f"+{count} {animal}")
            else:
                print(f"Not enough {animal} available")

        return True, ", ".join(message) if message else "No animals to take!"
