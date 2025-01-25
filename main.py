import pygame as py

from src.GUI.Navbar import Navbar
from src.actions.interactions import is_mouse_over, is_mouse_over_list
from src.GUI.Menu import Menu
from src.classes.Board import Board
from src.classes.Dice import Dice
from src.classes.Player import Player
from src.logic.GameLogic import GameLogic


class App:
    def __init__(self) -> None:
        """
        Initialize the application.
        """
        self.game_logic = None
        self.no_players = None
        self._running = True
        self.menu_shown = True
        self.menu = None
        self.game_end = False
        self._display_surf = None
        self.board_shown = False
        self.size = self.weight, self.height = 1600, 1600 / 16 * 9
        self.game_started = False
        self.font_title = None
        self.font_button = None
        self.navbar = None
        self.dice1 = None
        self.dice2 = None
        self.dice1_result = None
        self.dice2_result = None
        self.board = None
        self.player_turn = 0
        self.players = []

    def on_init(self):
        py.init()
        self._display_surf = py.display.set_mode(self.size, py.HWSURFACE | py.DOUBLEBUF)
        self._running = True
        try:
            self.font_title = py.font.Font("src/fonts/Poppins-Bold.ttf", 24)
            self.font_button = py.font.Font("src/fonts/Poppins-Medium.ttf", 20)
        except IOError:
            print("Font loading error, trying with default font...")
            self.font_title = py.font.Font(None, 24)
            self.font_button = py.font.Font(None, 20)
        except Exception as e:
            print(f"Error: {e}")
            print("Quitting...")
            self._running = False
            return False

    def on_event(self, event):
        # Window events
        if event.type == py.QUIT:
            self._running = False
        # Keyboard events
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                self._running = False
            elif self.menu_shown and self.menu:
                self.menu.handle_event(event)
        # Mouse events
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.menu_shown:
                self.no_players = self.menu.handle_event(event)
                if is_mouse_over_list(self.menu.player_buttons):
                    self.menu_shown = False
                    self.game_end = False
                    self.board_shown = True

                    self.navbar = Navbar(self._display_surf, 100, self.font_button, self.font_title, self.size)
                    self.board = Board(self.font_button, self.no_players)
                    for number in range(self.no_players):
                        player = Player(f"Player {number + 1}")
                        print(player.__str__())
                        self.players.append(player)
                    self.game_logic = GameLogic(self.players, self.navbar, self.board)
                    self.board.set_players(self.players)

                    # TODO: Init board and first player turn

            elif self.board_shown:
                if is_mouse_over(self.navbar.end_game_button):
                    self._running = False
                    print("Exit clicked")

                # TODO: Buttons for dice and exchange
                elif is_mouse_over(self.navbar.dice_button):
                    self.game_logic.roll_dice()
                    # # Roll the dices and update navbar
                    # self.dice1_result = self.dice1.roll()
                    # self.dice2_result = self.dice2.roll()
                    # self.navbar.set_dice_images(self.dice1_result, self.dice2_result)
                    # self.navbar.render_navbar()
                    # print(f"Dice 1: {self.navbar.dice1_image_name}, Dice 2: {self.navbar.dice2_image_name}")
                    pass
                elif is_mouse_over(self.navbar.exchange_button):
                    pass

        elif not self.game_end and not self.menu_shown:
            pass

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))

        # Menu rendering
        if self.menu_shown:
            self.menu = Menu(self.font_button)
            self.menu.create_menu(self._display_surf)

        if self.board_shown:
            self.navbar.render_navbar()
            self.board.render_board(self._display_surf, 100, self.size)

        py.display.flip()

    def on_cleanup(self):
        py.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            events = py.event.get()

            for event in events:
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
