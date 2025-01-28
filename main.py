import pygame as py

from src.GUI.Navbar import Navbar
from src.actions.interactions import is_mouse_over, is_mouse_over_list
from src.GUI.Menu import Menu
from src.classes.Board import Board
from src.classes.Dice import Dice
from src.classes.Player import Player
from src.logic.GameLogic import GameLogic
from src.classes.MainHerd import MainHerd
from src.GUI.MainHerdPanel import MainHerdPanel
from src.classes.TradeManager import TradeManager


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
        self.main_herd = MainHerd()
        self.herd_panel = None
        self.navbar_height = 100
        self.herd_panel_height = 100
        self.size = self.weight, self.height = 1600, 1600 / 16 * 9 + 100

    def on_init(self):
        py.init()
        self._display_surf = py.display.set_mode(self.size)
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

                    self.navbar = Navbar(self._display_surf, self.navbar_height, self.font_button, self.font_title, self.size)
                    self.trade_manager = TradeManager(self.main_herd)
                    
                    
                    self.board = Board(self.font_button, self.no_players, self.main_herd)
                    for number in range(self.no_players):
                        player = Player(f"Player {number + 1}", self.main_herd)
                        # add one rabbit from main herd to each player
                        player.add_animal("rabbit", 1)
                        print(player.__str__())
                        self.players.append(player)
                    self.game_logic = GameLogic(self.players, self.navbar, self.board, self.trade_manager)
                    self.herd_panel = MainHerdPanel(self._display_surf, self.font_button, [self.weight, self.navbar_height + self.herd_panel_height], self.game_logic, self.herd_panel_height)
                    self.herd_panel.set_main_herd(self.main_herd)

                    self.board.set_players(self.players)

                    # TODO: Init board and first player turn

            elif self.board_shown:
                self.herd_panel.handle_click(mouse_pos)
                if is_mouse_over(self.navbar.end_game_button):
                    self._running = False
                    print("Exit clicked")

                # TODO: Buttons for dice and exchange
                elif is_mouse_over(self.navbar.dice_button):
                    self.game_logic.roll_dice()
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
            # Render in this order:
            # 1. Navbar (at top)
            self.navbar.render_navbar()
            # 2. MainHerdPanel (after navbar)
            self.herd_panel.render_panel()
            # 2. Game boards (after navbar and MainHerdPanel)
            self.board.render_board(self._display_surf, self.navbar_height + self.herd_panel_height, self.size)
    
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
