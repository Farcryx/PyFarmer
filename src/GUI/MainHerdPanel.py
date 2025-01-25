import pygame as py
from typing import Tuple
from src.classes.MainHerd import MainHerd

class MainHerdPanel:
    PANEL_HEIGHT = 50  # Make this a class constant

    def __init__(self, window: py.Surface, font: py.font.Font, size: Tuple[int, int]) -> None:
        self.window = window
        self.font = font
        self.size = size
        self.panel_height = MainHerdPanel.PANEL_HEIGHT
        self.padding = 10
        self.main_herd = None

    def set_main_herd(self, main_herd: MainHerd) -> None:
        """Set the main herd reference"""
        self.main_herd = main_herd

    def draw_panel_background(self) -> None:
        """Draw the background of the herd panel"""
        panel_rect = (0, self.size[1] - self.panel_height, self.size[0], self.panel_height)
        py.draw.rect(self.window, (50, 50, 50), panel_rect)
        py.draw.rect(self.window, (100, 100, 100), panel_rect, 2)

    def render_animals_info(self) -> None:
        """Render information about animals in the main herd"""
        if not self.main_herd:
            return

        x_pos = self.padding
        y_pos = self.size[1] - self.panel_height + self.padding
        
        for animal, count in self.main_herd.herd.items():
            text = f"{animal}: {count}"
            text_surface = self.font.render(text, True, (255, 255, 255))
            self.window.blit(text_surface, (x_pos, y_pos))
            x_pos += text_surface.get_width() + 20  # Add spacing between items

    def render_panel(self) -> None:
        """Main method to render the entire panel"""
        self.draw_panel_background()
        self.render_animals_info()