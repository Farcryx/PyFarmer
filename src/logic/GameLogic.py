from src.classes.Dice import Dice
from src.classes.DiceEventHandler import DiceEventHandler
from src.classes.Player import Player
from src.GUI.Navbar import Navbar
from src.classes.Board import Board
from src.scripts.setup_game import DICE1_SIDES, DICE2_SIDES


class GameLogic():
    def __init__(self, players: [Player], navbar: Navbar, board: Board) -> None:
        """
        Initialize the game logic.
        :param players: List of players in the game.
        :param navbar: Navigation bar of the game.
        :param board: Board of the game.
        """
        self.players = players
        self.no_players = len(players)
        self.player_turn = 0
        self.dice1 = Dice(DICE1_SIDES, "dice1")
        self.dice2 = Dice(DICE2_SIDES, "dice2")
        self.dice1_result = None
        self.dice2_result = None
        self.navbar = navbar
        self.board = board
        self.dice_handler = DiceEventHandler(board.main_herd)

    def next_player(self) -> None:
        """
        Function that changes the player's turn.
        """
        self.player_turn = (self.player_turn + 1) % self.no_players
        self.check_turn()

    def roll_dice(self) -> None:
        """
        Function that rolls the dice and handles the result.
        """
        self.dice1_result = self.dice1.roll()
        self.dice2_result = self.dice2.roll()
        self.navbar.set_dice_images(self.dice1_result, self.dice2_result)
        self.navbar.render_navbar()
        self.players[self.player_turn].current_dice_roll = (self.dice1_result, self.dice2_result)
        print(self.players[self.player_turn].get_last_roll())
        handle_roll = self.dice_handler.handle_roll(self.dice1_result, self.dice2_result, self.players[self.player_turn])
        print(handle_roll)
        self.next_player()

    def check_turn(self) -> None:
        """
        Function that check which player's turn is it and adds stroke to the player's board.
        """
        for i in range(self.no_players):
            if i == self.player_turn:
                self.board.add_stroke(i)

    def exchange_dice(self):
        pass

    def end_turn(self):
        pass

    def end_game(self):
        pass
