import pygame as py
from typing import List, Tuple

from src.classes import Player
from src.classes.MainHerd import MainHerd
from src.enums.Animal import Animal


class Board:
    """
    Class that represents the board of the game.
    """

    def __init__(self, font: py.font.Font, no_players: int, main_herd: MainHerd) -> None:
        """
        Initialize the board.
        :param font: Font used for rendering text.
        :param no_players: Number of players in the game.
        """
        self.font = font
        self.no_players = no_players
        self.animals_coords = None
        self.positions = None
        self.board_width = None
        self.board_height = None
        self.window = None
        self.active_player = 0
        self.players = []
        self.render_player = 0
        self.main_herd = main_herd
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

    def load_and_scale_board_image(self, size: tuple[int, float], nav_bar_height: int) -> List[py.Surface]:
        """
        Load and scale the board image based on the number of players.
        :param size: Size of the window.
        :param nav_bar_height: Height of the navigation bar.
        :return: Scaled board image.
        """
        board_image = py.image.load('src/images/wood_texture.jpg')
        boards = []

        if self.no_players == 1:
            return [py.transform.smoothscale(board_image, (size[0], size[1] - nav_bar_height))]
        for num_of_player in range(self.no_players):
            # Load and scale the images of the animals and place them on the board
            for i in range(5):
                animal_count = self.players[num_of_player].get_number_of_animal(Animal(i).name.lower())
                image_active = py.image.load(f'src/images/animals-active/{Animal(i).name.lower()}.png')
                image_inactive = py.image.load(f'src/images/animals/{Animal(i).name.lower()}.png')
                image_active = py.transform.smoothscale(image_active, (80 * 2, 80 * 2))
                image_inactive = py.transform.smoothscale(image_inactive, (80 * 2, 80 * 2))
                height = self.board_height - 250 + 200 * i

                # ISSUE: The text is repeatedly superimposed on itself.
                #  This leads to a frequently visible layer that is underneath the actual text.
                # Text rendering
                font_size = 64  # Adjust the font size as needed
                self.font = py.font.Font(None, font_size)
                text = self.font.render(str(animal_count), True, (0, 0, 0))
                text_rect = text.get_rect()
                padding = 10  # Adjust the padding as needed
                text_rect.topleft = (self.board_width - 380 + 100 * i, height)
                # Clear the previous text by drawing a rectangle with the background color and padding
                background_rect = py.Rect(text_rect.left - padding, text_rect.top - padding, text_rect.width + 2 * padding, text_rect.height + 2 * padding)
                board_image.fill((255, 255, 255), background_rect)
                board_image.blit(text, text_rect.topleft)

                for j in range(5 - i):
                    width = self.board_width - 240 + 200 * j + 100 * i
                    self.animals_coords[1][Animal(i)].append((width, height))
                    # render the animals on the board
                    if animal_count > 0:
                        board_image.blit(image_active, (width - 40 * 2, height - 40 * 2))
                        animal_count -= 1
                    else:
                        board_image.blit(image_inactive, (width - 40 * 2, height - 40 * 2))

            # Render two dogs on the board
            # check if the player has small dog
            if self.players[num_of_player].get_number_of_animal(Animal.SMALL_DOG.name.lower()) > 0:
                small_dog = py.image.load('src/images/animals-active/small_dog.png')
            else:
                small_dog = py.image.load('src/images/animals/small_dog.png')
            
            if self.players[num_of_player].get_number_of_animal(Animal.BIG_DOG.name.lower()) > 0:
                big_dog = py.image.load('src/images/animals-active/big_dog.png')
            else:
                big_dog = py.image.load('src/images/animals/big_dog.png')
            small_dog = py.transform.smoothscale(small_dog, (80 * 2, 80 * 2))
            big_dog = py.transform.smoothscale(big_dog, (80 * 2, 80 * 2))
            for i in range(2):
                width = self.board_width - 240 + 200 * i
                self.animals_coords[1][Animal(5 + i)].append((width, height))
                if i == 0:
                    board_image.blit(small_dog, (width - 40 * 10, self.board_height - 250 + 200 * 4 - 80))
                else:
                    board_image.blit(big_dog, (width - 40 * 10, self.board_height - 250 + 200 * 4 - 80))
            boards.append(py.transform.smoothscale(board_image, (self.board_width, self.board_height)))

        return boards

    def render_board(self, window: py.Surface, nav_bar_height: int, size: tuple[int, float]) -> None:
        """
        Render the board on the screen.
        :param nav_bar_height: Height of the navigation bar.
        :param size: Size of the window.
        :param window: Surface to render the board on.
        """
        self.board_width = size[0] // 2
        self.board_height = (size[1] - nav_bar_height) // 2
        board_image = self.load_and_scale_board_image(size, nav_bar_height)
        positions = self.get_board_positions(nav_bar_height, self.board_width, self.board_height)
        self.positions = positions
        self.window = window
        for i in range(self.no_players):
            window.blit(board_image[i], positions[i])

        # for pos in positions:
        #     window.blit(board_image, pos)
        if self.active_player is not None:
            # draw stroke for active player
            py.draw.rect(self.window, (196, 246, 255), (self.positions[self.active_player][0], self.positions[self.active_player][1], self.board_width, self.board_height), 5)
            # remove stroke for other players
            for i in range(self.no_players):
                if i != self.active_player:
                    py.draw.rect(self.window, (0, 0, 0), (self.positions[i][0], self.positions[i][1], self.board_width, self.board_height), 5)

    def add_stroke(self, player: int) -> None:
        """
        Add a stroke to the board of the player.
        :param player: Index of the player.
        """
        self.active_player = player

    def set_players(self, players: [Player]) -> None:
        """
        Set the players of game.
        :param players: List of players in the game.
        """
        self.players = players
