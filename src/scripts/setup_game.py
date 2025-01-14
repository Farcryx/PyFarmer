# Setup new game script
from src.classes.Animal import Animal
from src.classes.Player import Player
from src.classes.Dice import Dice
from src.classes.TradeManager import TradeManager
from src.classes.DiceEventHandler import DiceEventHandler

# Game constants
INITIAL_HERD = {
    "królik": 60,
    "owca": 24,
    "świnia": 20,
    "krowa": 12,
    "koń": 6
}

EXCHANGE_RATES = {
    "królik": {"owca": 6, "świnia": 12, "krowa": 36, "koń": 72},
    "owca": {"królik": 1 / 6, "świnia": 2, "krowa": 6, "koń": 12},
    "świnia": {"królik": 1 / 12, "owca": 1 / 2, "krowa": 3, "koń": 6},
    "krowa": {"królik": 1 / 36, "owca": 1 / 6, "świnia": 1 / 3, "koń": 2},
    "koń": {"królik": 1 / 72, "owca": 1 / 12, "świnia": 1 / 6, "krowa": 1 / 2}
}

DICE1_SIDES = ["królik", "królik", "królik", "królik", "królik", "królik", "królik", "królik", "owca", "świnia",
               "krowa", "lis"]
DICE2_SIDES = ["królik", "królik", "królik", "królik", "królik", "królik", "królik", "królik", "owca", "świnia", "koń",
               "wilk"]


def create_animals():
    """Create all animal objects with initial values"""
    return {
        "królik": Animal("królik", 1, INITIAL_HERD["królik"], "prey"),
        "owca": Animal("owca", 6, INITIAL_HERD["owca"], "farm"),
        "świnia": Animal("świnia", 12, INITIAL_HERD["świnia"], "farm"),
        "krowa": Animal("krowa", 36, INITIAL_HERD["krowa"], "farm"),
        "koń": Animal("koń", 72, INITIAL_HERD["koń"], "farm")
    }


def create_players(num_players: int) -> list[Player]:
    """Create specified number of players"""
    return [Player(f"Gracz {i + 1}") for i in range(num_players)]


def create_dice() -> tuple[Dice, Dice]:
    """Create game dice"""
    dice1 = Dice(DICE1_SIDES, "dice1")
    dice2 = Dice(DICE2_SIDES, "dice2")
    return dice1, dice2


def setup_game(num_players: int = 2):
    """Initialize complete game setup"""
    # Create main game components
    animals = create_animals()
    players = create_players(num_players)
    dice1, dice2 = create_dice()

    # Create trade manager
    trade_manager = TradeManager(EXCHANGE_RATES, INITIAL_HERD)

    # Create dice event handler for first player (will be updated during game)
    dice_handler = DiceEventHandler(
        INITIAL_HERD,
        players[0].animals,
        {"small_dog": players[0].small_dogs, "big_dog": players[0].big_dogs}
    )

    game_state = {
        "animals": animals,
        "players": players,
        "dice": (dice1, dice2),
        "trade_manager": trade_manager,
        "dice_handler": dice_handler,
        "current_player": 0,
        "game_started": False
    }

    return game_state


if __name__ == "__main__":
    # Test game setup
    game = setup_game(4)
    print(f"Game initialized with {len(game['players'])} players")
    print("Main herd:", INITIAL_HERD)
    print("First player:", game["players"][0])
