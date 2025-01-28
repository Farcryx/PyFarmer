import pygame as py
from typing import Tuple

class Navbar:
    def __init__(self, window: py.Surface, nav_bar_height: int, font_button: py.font.Font, font_title: py.font.Font, size: Tuple[int, float]) -> None:
        self.window = window
        self.nav_bar_height = nav_bar_height
        self.font_button = font_button
        self.font_title = font_title
        self.size = size
        self.dice_button = None
        self.end_game_button = None
        self.dice1_image_name = None
        self.dice2_image_name = None

    def draw_navbar_background(self) -> None:
        """
        Method drawing the background of the navigation bar.
        """
        py.draw.rect(self.window, (50, 50, 50), (0, 0, self.size[0], self.nav_bar_height))

    def render_game_name(self) -> None:
        """
        Method rendering the game name on the navigation bar.
        """
        game_name = "PyFarmer"
        text_surface = self.font_title.render(game_name, True, (255, 255, 255))
        self.window.blit(text_surface, (10, 30))

    def render_button(self, text: str, x: int, y: int, width: int, height: int) -> py.Rect:
        """
        Method rendering a button on the navigation bar.
        :param text: Text displayed on the button.
        :param x: X-coordinate of the button.
        :param y: Y-coordinate of the button.
        :param width: Width of the button.
        :param height: Height of the button.
        :return: Rectangle of the button.
        """
        button_rect = py.draw.rect(self.window, (100, 100, 100), (x, y, width, height))
        text_surface = self.font_button.render(text, True, (255, 255, 255))
        self.window.blit(text_surface, (x + 10, y + 10))
        return button_rect

    def set_dice_images(self, dice1_image_name: str, dice2_image_name: str) -> None:
        """
        Method setting the dice images on the navigation bar.
        """
        self.dice1_image_name = dice1_image_name
        self.dice2_image_name = dice2_image_name

    def render_dice_images(self, x1: int, x2: int) -> None:
        """
        Method rendering the dice images on the navigation bar.
        """
        if self.dice1_image_name and self.dice2_image_name:
            image1 = py.image.load(f'src/images/animals/{self.dice1_image_name.lower()}.png')
            image1 = py.transform.smoothscale(image1, (60, 60))  # Adjust the size as needed
            self.window.blit(image1, (x1, 20))

            image2 = py.image.load(f'src/images/animals/{self.dice2_image_name.lower()}.png')
            image2 = py.transform.smoothscale(image2, (60, 60))  # Adjust the size as needed
            self.window.blit(image2, (x2, 20))

    def render_navbar(self) -> None:
        """
        Method rendering the navigation bar.
        """
        self.draw_navbar_background()
        self.render_game_name()

        button_width = 200
        button_height = 50
        padding = 10

        start_game_button_x = self.size[0] - button_width - padding
        dice_button_x = start_game_button_x - button_width - padding
        dice_result1_x = dice_button_x - 100 - padding
        dice_result2_x = dice_result1_x - 100 - padding

        self.dice_button = self.render_button("RZUT KOSTKĄ", dice_button_x, 25, button_width, button_height)
        self.end_game_button = self.render_button("ZAKOŃCZ GRĘ", start_game_button_x, 25, button_width, button_height)
        self.render_dice_images(dice_result1_x, dice_result2_x)