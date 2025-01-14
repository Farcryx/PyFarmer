import pygame as py

from src.actions.interactions import is_mouse_over
from src.scripts.setup_game import create_players
from src.GUI.Menu import Menu


class App:
    def __init__(self, no_players: int = 4) -> None:
        """
        Inicjalizacja aplikacji
        :param no_players: Liczba graczy w grze (stała = 4)
        """
        self.players = create_players(no_players)
        self._running = True
        self.menu_shown = True
        self.menu = None
        self.game_end = False
        self._display_surf = None
        self.size = self.weight, self.height = 1600, 1600 / 16 * 9
        self.game_started = False

    def on_init(self):
        py.init()
        self._display_surf = py.display.set_mode(self.size, py.HWSURFACE | py.DOUBLEBUF)
        self._running = True
        self.font_title = py.font.SysFont('Poppins', 24, bold=True)  # Dodaj czcionkę
        self.font_button = py.font.SysFont('Poppins', 20, bold=True)  # Czcionka dla przycisków

    def on_event(self, event):
        # Window events
        if event.type == py.QUIT:
            self._running = False
        # Keyboard events
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                self._running = False
        # Mouse events
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.menu_shown:
                if is_mouse_over(self.menu.start_button):
                    self.menu_shown = False
                    self.game_end = False
                    print("Start clicked")
                    # TODO: Inicjalizacja planszy gry i wybór użytkownika, który ma rozpocząć grę
                elif is_mouse_over(self.menu.exit_button):
                    self._running = False
                    print("Exit clicked")




        elif not self.game_end and not self.menu_shown:
            pass

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))  # Wyczyść ekran na czarno

        # Wysokość paska nawigacyjnego
        nav_bar_height = 100

        # Narysuj pasek nawigacyjny
        py.draw.rect(self._display_surf, (50, 50, 50), (0, 0, self.size[0], nav_bar_height))

        # Renderuj nazwę gry
        game_name = "PyFarmer"
        text_surface = self.font_title.render(game_name, True, (255, 255, 255))
        self._display_surf.blit(text_surface, (10, 30))  # Wyświetl tekst w lewym rogu paska nawigacyjnego

        # Renderuj przyciski
        dice_button_text = self.font_button.render("RZUT KOSTKĄ", True, (255, 255, 255))
        exchange_button_text = self.font_button.render("WYMIANA", True, (255, 255, 255))
        start_game_button_text = self.font_button.render("ZAKOŃCZ GRĘ", True, (255, 255, 255))

        # Pozycje przycisków
        button_width = 200
        button_height = 50
        padding = 10

        start_game_button_x = self.size[0] - button_width - padding
        exchange_button_x = start_game_button_x - button_width - padding
        dice_button_x = exchange_button_x - button_width - padding

        self.start_game_button_rect = py.draw.rect(self._display_surf, (100, 100, 100),
                                                   (start_game_button_x, 25, button_width, button_height))
        self.exchange_button_rect = py.draw.rect(self._display_surf, (100, 100, 100),
                                                 (exchange_button_x, 25, button_width, button_height))
        self.dice_button_rect = py.draw.rect(self._display_surf, (100, 100, 100),
                                             (dice_button_x, 25, button_width, button_height))

        # Wyświetl tekst na przyciskach
        self._display_surf.blit(dice_button_text, (dice_button_x + 10, 35))
        self._display_surf.blit(exchange_button_text, (exchange_button_x + 10, 35))
        self._display_surf.blit(start_game_button_text, (start_game_button_x + 10, 35))

        # Rozmiar każdej planszy
        board_width = self.size[0] // 2
        board_height = (self.size[1] - nav_bar_height) // 2

        # Pozycje plansz
        positions = [
            (0, nav_bar_height),  # Lewy górny róg
            (board_width, nav_bar_height),  # Prawy górny róg
            (0, nav_bar_height + board_height),  # Lewy dolny róg
            (board_width, nav_bar_height + board_height)  # Prawy dolny róg
        ]

        # Załaduj obraz planszy
        board_image = py.image.load('src/images/plansza_16_9.jpg')
        board_image = py.transform.smoothscale(board_image, (board_width, board_height))

        # Narysuj każdą planszę
        for pos in positions:
            self._display_surf.blit(board_image, pos)

        if self.menu_shown:
            self.menu = Menu(self.font_button)
            self.menu.create_menu(self._display_surf)

        py.display.flip()  # Odśwież ekran

    def on_cleanup(self):
        py.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in py.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
