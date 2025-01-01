import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1600, 1600/16*9

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.font_title = pygame.font.SysFont('Poppins', 24, bold=True)  # Dodaj czcionkę

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

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
