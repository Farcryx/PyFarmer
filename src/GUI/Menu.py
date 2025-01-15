import pygame as py


class Menu:
    """
    Class representing the game menu.
    """

    def __init__(self, font: py.font.Font) -> None:
        """
        Initialize the menu.
        :param font: Font to be used in the menu.
        """
        self.player_buttons = []
        self.font = font
        self.menu_items = ["Start", "Exit"]
        self.menu_spacing = 10

    def create_menu(self, window: py.Surface) -> None:
        """
        Create the game menu.
        :param window: Surface on which the menu is to be displayed.
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

        # Create player buttons
        button_width = 200
        button_height = 50
        button_labels = ["2 Players", "3 Players", "4 Players"]

        for i, label in enumerate(button_labels):
            button_rect = (
                window.get_width() // 2 - 300 + i * (button_width + 20),
                window.get_height() // 2 + 100,
                button_width,
                button_height,
            )
            self.player_buttons.append(button_rect)
            py.draw.rect(window, (100, 100, 100), button_rect)
            button_text = self.font.render(label, True, (255, 255, 255))
            window.blit(
                button_text,
                (button_rect[0] + (button_width - button_text.get_width()) // 2, button_rect[1] + 10)
            )

        py.display.flip()

    def handle_event(self, event: py.event.EventType) -> int | None:
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = py.mouse.get_pos()
            for i, rect in enumerate(self.player_buttons):
                if (rect[0] <= mouse_x <= rect[0] + rect[2] and
                        rect[1] <= mouse_y <= rect[1] + rect[3]):
                    # Handle selection for player button i
                    print(f"Selected {i + 2} players.")
                    return i + 2

