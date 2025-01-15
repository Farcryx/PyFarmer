import pygame as py
from typing import List, Tuple
from src.enums.Animal import Animal


class Board:
    """
    Class that represents the board of the game.
    """

    def __init__(self, font: py.font.Font, no_players: int) -> None:
        """
        Initialize the board.
        :param font: Font used for rendering text.
        :param no_players: Number of players in the game.
        """
        self.font = font
        self.no_players = no_players
        self.animals_coords = None

    def get_board_positions(self, nav_bar_height: int, board_width: int, board_height: float) -> List[
        Tuple[int, float]]:
        """
        Get the positions of the boards based on the number of players.
        :param nav_bar_height: Height of the navigation bar.
        :param board_width: Width of each board.
        :param board_height: Height of each board.
        :return: List of positions for the boards.
        """
        positions = {
            4: [
                (0, nav_bar_height),
                (board_width, nav_bar_height),
                (0, nav_bar_height + board_height),
                (board_width, nav_bar_height + board_height)
            ],
            3: [
                (0, nav_bar_height),
                (board_width, nav_bar_height),
                (0, nav_bar_height + board_height)
            ],
            2: [
                (0, nav_bar_height),
                (board_width, nav_bar_height)
            ],
            1: [
                (0, nav_bar_height)
            ]
        }
        return positions.get(self.no_players, [(0, nav_bar_height)])

    def load_and_scale_board_image(self, size: tuple[int, float], nav_bar_height: int) -> py.Surface:
        """
        Load and scale the board image based on the number of players.
        :param size: Size of the window.
        :param nav_bar_height: Height of the navigation bar.
        :return: Scaled board image.
        """
        board_image = py.image.load('src/images/wood_texture.jpg')

        self.animals_coords = [
            {
                Animal.RABBIT: [],
                Animal.SHEEP: [],
                Animal.PIG: [],
                Animal.COW: [],
                Animal.HORSE: [],
                Animal.SMALL_DOG: [],
                Animal.BIG_DOG: [],
            }
            for _ in range(self.no_players)
        ]

        if self.no_players == 1:
            return py.transform.smoothscale(board_image, (size[0], size[1] - nav_bar_height))

        # Calculate the size of the board
        board_width = size[0] // 2
        board_height = (size[1] - nav_bar_height) // 2

        # Load and scale the images of the animals and place them on the board
        for i in range(5):
            image = py.image.load(f'src/images/zwierzaki/{Animal(i).name.lower()}.png')
            image = py.transform.smoothscale(image, (80 * 2, 80 * 2))  # Adjust the size as needed
            height = board_height - 250 + 200 * i
            for j in range(5 - i):
                width = board_width - 240 + 200 * j + 100 * i
                self.animals_coords[1][Animal(i)].append((width, height))
                board_image.blit(image, (width - 40 * 2, height - 40 * 2))  # Adjust position to center the image

        # Render two dogs on the board
        small_dog = py.image.load('src/images/zwierzaki/small_dog.png')
        big_dog = py.image.load('src/images/zwierzaki/big_dog.png')
        small_dog = py.transform.smoothscale(small_dog, (80 * 2, 80 * 2))
        big_dog = py.transform.smoothscale(big_dog, (80 * 2, 80 * 2))
        for i in range(2):
            width = board_width - 240 + 200 * i
            self.animals_coords[1][Animal(5 + i)].append((width, height))
            if i == 0:
                board_image.blit(small_dog, (width - 40 * 10, board_height - 250 + 200 * 4 - 80))
            else:
                board_image.blit(big_dog, (width - 40 * 10, board_height - 250 + 200 * 4 - 80))

        return py.transform.smoothscale(board_image, (board_width, board_height))

    def render_board(self, window: py.Surface, nav_bar_height: int, size: tuple[int, float]) -> None:
        """
        Render the board on the screen.
        :param nav_bar_height: Height of the navigation bar.
        :param size: Size of the window.
        :param window: Surface to render the board on.
        """
        board_width = size[0] // 2
        board_height = (size[1] - nav_bar_height) // 2
        board_image = self.load_and_scale_board_image(size, nav_bar_height)
        positions = self.get_board_positions(nav_bar_height, board_width, board_height)
        for pos in positions:
            window.blit(board_image, pos)

    def add_stroke(self, player: int) -> None:
        """
        Add a stroke to the board of the player.
        :param player: Index of the player.
        """
        pass

    def remove_stroke(self, player: int) -> None:
        """
        Remove a stroke from the board of the player.
        :param player: Index of the player.
        """
        pass
