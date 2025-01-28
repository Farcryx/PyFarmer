from src.classes.Player import Player
from src.classes.MainHerd import MainHerd
from src.scripts.setup_game import EXCHANGE_RATES


class TradeManager:
    def __init__(self, main_herd: MainHerd):
        self.exchange_rates = EXCHANGE_RATES
        self.main_herd = main_herd
        self.exchange_list = [
            ["rabbit", "sheep"],
            ["sheep", "pig"],
            ["pig", "cow"],
            ["cow", "horse"],
            ["sheep", "small_dog"],
            ["cow", "big_dog"]
        ]

    def can_trade(self, source_animal: str, target_animal: str, quantity: int, player_animals: dict) -> bool:
        """Check if trade is possible based on exchange rates and quantities"""
        if source_animal not in self.exchange_rates or target_animal not in self.exchange_rates[source_animal]:
            return False
        
        required_quantity = self.exchange_rates[source_animal][target_animal] * quantity
        return (player_animals[source_animal] >= required_quantity and 
                self.main_herd[target_animal] >= quantity)

    def execute_trade(self, source_animal: str, target_animal: str, player: 'Player', quantity: int = 1) -> bool:
        """Execute trade between animals"""
        if not self.can_trade(source_animal, target_animal, quantity, player.animals):
            return False

        required_quantity = self.exchange_rates[source_animal][target_animal] * quantity
        
        # Update player's animals
        player.animals[source_animal] -= required_quantity
        player.animals[target_animal] += quantity
        
        # Update main herd
        self.main_herd[target_animal] -= quantity
        self.main_herd[source_animal] += required_quantity
        
        return True
    
    def gui_check_exchange(self, source_animal: str, target_animal: str, player: Player) -> bool:
        """
        Based on player's animals and main herd animals, check if exchange is possible due to exchange rates.
        param source_animal: Source animal type.
        param target_animal: Target animal type.
        param player: Player object.
        return: True if exchange is possible, False otherwise.
        """

        if source_animal not in self.exchange_rates or target_animal not in self.exchange_rates[source_animal]:
            return False
        
        required_quantity = self.exchange_rates[source_animal][target_animal]
        
        # check if player has small dog, if yes, exchange for small dog is not possible
        if source_animal == "sheep" and player.animals.get("small_dog", 0) > 0:
            return False
        if source_animal == "cow" and player.animals.get("big_dog", 0) > 0:
            return False

        return (player.animals[source_animal] >= required_quantity and 
                self.main_herd[target_animal] > 0)