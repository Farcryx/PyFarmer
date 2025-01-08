from classes import Player


class TradeManager:
    def __init__(self, exchange_rates: dict[str, dict[str, int]], main_herd: dict[str, int]):
        self.exchange_rates = exchange_rates
        self.main_herd = main_herd

    def can_trade(self, source_animal: str, target_animal: str, quantity: int, player_animals: dict) -> bool:
        """Check if trade is possible based on exchange rates and quantities"""
        if source_animal not in self.exchange_rates or target_animal not in self.exchange_rates[source_animal]:
            return False
        
        required_quantity = self.exchange_rates[source_animal][target_animal] * quantity
        return (player_animals[source_animal] >= required_quantity and 
                self.main_herd[target_animal] >= quantity)

    def execute_trade(self, source_animal: str, target_animal: str, quantity: int, player: 'Player') -> bool:
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

    def buy_dog(self, dog_type: str, player: 'Player') -> bool:
        """Buy a dog for the player"""
        cost = 6 if dog_type == "small" else 12  # małe psy kosztują 6 owiec, duże 12
        
        if player.animals["owca"] >= cost:
            player.animals["owca"] -= cost
            if dog_type == "small":
                player.small_dogs += 1
            else:
                player.big_dogs += 1
            return True
        return False