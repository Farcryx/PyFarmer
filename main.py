import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1600, 1600/16*9
        self.game_started = False

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.font_title = pygame.font.SysFont('Poppins', 24, bold=True)  # Dodaj czcionkę
        self.font_button = pygame.font.SysFont('Poppins', 20, bold=True)  # Czcionka dla przycisków



    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.dice_button_rect.collidepoint(mouse_pos):
                print("Rzut kostką clicked")
            elif self.exchange_button_rect.collidepoint(mouse_pos):
                print("Wymiana clicked")
            elif self.start_game_button_rect.collidepoint(mouse_pos):
                if self.game_started:
                    print("Zakończono grę")
                    self.game_started = False
                else:
                    print("Rozpoczęto grę")
                    self.game_started = True

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))  # Wyczyść ekran na czarno

        # Wysokość paska nawigacyjnego
        nav_bar_height = 100

        # Narysuj pasek nawigacyjny
        pygame.draw.rect(self._display_surf, (50, 50, 50), (0, 0, self.size[0], nav_bar_height))

        # Renderuj nazwę gry
        game_name = "PyFarmer"
        text_surface = self.font_title.render(game_name, True, (255, 255, 255))
        self._display_surf.blit(text_surface, (10, 30))  # Wyświetl tekst w lewym rogu paska nawigacyjnego

        # Renderuj przyciski
        dice_button_text = self.font_button.render("RZUT KOSTKĄ", True, (255, 255, 255))
        exchange_button_text = self.font_button.render("WYMIANA", True, (255, 255, 255))
        start_game_button_text = self.font_button.render("ZAKOŃCZ GRĘ" if self.game_started else "ROZPOCZNIJ GRĘ", True, (255, 255, 255))

        # Pozycje przycisków
        button_width = 200
        button_height = 50
        padding = 10

        start_game_button_x = self.size[0] - button_width - padding
        exchange_button_x = start_game_button_x - button_width - padding
        dice_button_x = exchange_button_x - button_width - padding

        self.start_game_button_rect = pygame.draw.rect(self._display_surf, (100, 100, 100), (start_game_button_x, 25, button_width, button_height))
        self.exchange_button_rect = pygame.draw.rect(self._display_surf, (100, 100, 100), (exchange_button_x, 25, button_width, button_height))
        self.dice_button_rect = pygame.draw.rect(self._display_surf, (100, 100, 100), (dice_button_x, 25, button_width, button_height))

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
        board_image = pygame.image.load('src/images/plansza_16_9.jpg')
        board_image = pygame.transform.smoothscale(board_image, (board_width, board_height))

        # Narysuj każdą planszę
        for pos in positions:
            self._display_surf.blit(board_image, pos)

        pygame.display.flip()  # Odśwież ekran



    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
