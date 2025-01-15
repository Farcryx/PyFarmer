# Setup new game script
from src.classes.Animal import Animal
from src.classes.Player import Player
from src.classes.Dice import Dice
from src.classes.TradeManager import TradeManager
from src.classes.DiceEventHandler import DiceEventHandler

# Game constants
INITIAL_HERD = {
    "rabbit": 60,
    "sheep": 24,
    "pig": 20,
    "cow": 12,
    "horse": 6
}

EXCHANGE_RATES = {
    "rabbit": {"sheep": 6, "pig": 12, "cow": 36, "horse": 72},
    "sheep": {"rabbit": 1 / 6, "pig": 2, "cow": 6, "horse": 12},
    "pig": {"rabbit": 1 / 12, "sheep": 1 / 2, "cow": 3, "horse": 6},
    "cow": {"rabbit": 1 / 36, "sheep": 1 / 6, "pig": 1 / 3, "horse": 2},
    "horse": {"rabbit": 1 / 72, "sheep": 1 / 12, "pig": 1 / 6, "cow": 1 / 2}
}

DICE1_SIDES = ["rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "sheep", "pig",
               "cow", "fox"]
DICE2_SIDES = ["rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "sheep", "pig",
               "horse", "wolf"]


def create_animals():
    """Create all animal objects with initial values"""
    return {
        "rabbit": Animal("rabbit", 1, INITIAL_HERD["rabbit"], "prey"),
        "sheep": Animal("sheep", 6, INITIAL_HERD["sheep"], "farm"),
        "pig": Animal("pig", 12, INITIAL_HERD["pig"], "farm"),
        "cow": Animal("cow", 36, INITIAL_HERD["cow"], "farm"),
        "horse": Animal("horse", 72, INITIAL_HERD["horse"], "farm")
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
