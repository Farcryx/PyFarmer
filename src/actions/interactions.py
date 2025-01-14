import pygame as py


def is_mouse_over(rect: tuple[float, float, float, float]) -> bool:
    """
    Function checking whether mouse cursor is hovering over specified rectangle.
    :param rect: Checked rectangle.
    :return: (bool) True if mouse is over specified rectangle or False otherwise.
    """
    mouse_x, mouse_y = py.mouse.get_pos()
    return (
            rect[0] < mouse_x < rect[0] + rect[2] and rect[1] < mouse_y < rect[1] + rect[3]
    )