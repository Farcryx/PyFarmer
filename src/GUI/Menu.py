import pygame as py


class Menu:
    """
    Klasa reprezentująca menu gry.
    """

    def __init__(self, font: py.font.Font) -> None:
        """
        Inicjalizacja menu.
        :param font: Czcionka do wykorzystania w menu.
        """
        self.font = font
        self.menu_items = ["Start", "Exit"]

        self.menu_spacing = 10
        self.start_button = None
        self.exit_button = None

    def create_menu(self, window: py.Surface) -> None:
        """
        Tworzy menu gry.
        :param window: Powierzchnia, na której ma być wyświetlone menu.
        """
        menu_background = (
            window.get_width() // 4,
            window.get_height() // 4,
            window.get_width() // 2,
            window.get_height() // 2,

        )
        # Rectangle with stroke

        py.draw.rect(window, (50, 50, 50), menu_background)
        py.draw.rect(window, (255, 255, 255), menu_background, 5)

        # Welcome text
        welcome_text = self.font.render("Welcome to PyFarmer!", True, (255, 255, 255))
        window.blit(welcome_text, (menu_background[0] + 10, menu_background[1] + 10))

        # Create buttons
        self.start_button = (
            window.get_width() // 2 - 100,
            window.get_height() // 2 - 50,
            200,
            50,
        )

        self.exit_button = (
            window.get_width() // 2 - 100,
            window.get_height() // 2 + 10,
            200,
            50,
        )

        py.draw.rect(window, (100, 100, 100), self.start_button)
        py.draw.rect(window, (100, 100, 100), self.exit_button)

        # Button text
        start_text = self.font.render("Start", True, (255, 255, 255))
        exit_text = self.font.render("Exit", True, (255, 255, 255))

        window.blit(start_text, (self.start_button[0] + 10, self.start_button[1] + 10))
        window.blit(exit_text, (self.exit_button[0] + 10, self.exit_button[1] + 10))

        py.display.flip()
