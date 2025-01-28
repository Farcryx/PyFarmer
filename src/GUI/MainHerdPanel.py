import pygame as py
from typing import Tuple
from src.classes.MainHerd import MainHerd
from src.logic.GameLogic import GameLogic

class MainHerdPanel:
    PANEL_HEIGHT = 50  # Make this a class constant

    def __init__(self, window: py.Surface, font: py.font.Font, size: Tuple[int, int], game_logic: GameLogic) -> None:
        self.window = window
        self.font = font
        self.size = size
        self.panel_height = MainHerdPanel.PANEL_HEIGHT
        self.padding = 10
        self.main_herd = None
        self.exchange_buttons = {}
        self.button_width = 80
        self.button_height = 30
        self.game_logic = game_logic

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

    def render_exchange_buttons(self) -> None:
        """Render exchange buttons for animals"""
        if not self.main_herd:
            return

        x_pos = self.padding + 505
        y_pos = self.size[1] - self.panel_height + self.padding
        
        self.render_animals_info()
        
        for count, exchange in enumerate(self.game_logic.trade_manager.exchange_list):
            button_rect = py.Rect(x_pos, y_pos, self.button_width + 110, self.button_height)
            
            # Button color based on exchange possibility
            button_color = (0, 200, 0) if self.game_logic.trade_manager.gui_check_exchange(exchange[0], exchange[1], self.game_logic.players[self.game_logic.player_turn]) else (150, 150, 150)
            py.draw.rect(self.window, button_color, button_rect)
            
            # Button text
            text = f"{exchange[0]}->{exchange[1].replace('_', ' ')}"
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.window.blit(text_surface, text_rect)
            
            # Store button for click detection
            self.exchange_buttons[(exchange[0], exchange[1])] = button_rect
            x_pos += self.button_width + 115

    def render_panel(self) -> None:
        """Main method to render the entire panel"""
        self.draw_panel_background()
        self.render_exchange_buttons()

    def handle_click(self, mouse_pos: Tuple[int, int]) -> None:
        """Handle mouse click events"""
        for (from_animal, to_animal), button_rect in self.exchange_buttons.items():
            if button_rect.collidepoint(mouse_pos):
                if self.main_herd.can_exchange(from_animal):
                    print(f"Exchange {from_animal} to {to_animal}")
                    # Call your exchange logic here
                    self.game_logic.trade_manager.execute_trade(from_animal, to_animal, self.game_logic.players[self.game_logic.player_turn])
                break